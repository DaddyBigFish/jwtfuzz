import sys
import jwt
import json
import getopt

def fuzz_jwt(payload_template, fuzz_file, secret_key, algorithm, output_file):
    with open(fuzz_file, 'r') as file:
        fuzz_values = file.readlines()

  fuzz_values = [value.strip() for value in fuzz_values]

    output_lines = []
  
    for fuzz_value in fuzz_values:
        payload = json.loads(json.dumps(payload_template))  

        def replace_fuzz(data):
            if isinstance(data, dict):
                for key, value in data.items():
                    if isinstance(value, (dict, list)):
                        replace_fuzz(value)  
                    elif value == "FUZZ":
                        data[key] = fuzz_value
            elif isinstance(data, list):
                for i in range(len(data)):
                    if isinstance(data[i], (dict, list)):
                        replace_fuzz(data[i])  
                    elif data[i] == "FUZZ":
                        data[i] = fuzz_value

        replace_fuzz(payload)

      token = jwt.encode(payload, secret_key, algorithm=algorithm)
      
        print(f"{fuzz_value:<20} {token}")
        output_lines.append(token)

    if output_file:
        with open(output_file, 'w') as out_file:
            out_file.write("\n".join(output_lines))

def parse_args():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hj:w:k:a:o:", ["jwt=", "w=", "key=", "algo=", "output="])
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(1)

    jwt_token = None
    fuzz_file = None
    secret_key = None
    algorithm = 'HS256'  # Default algorithm is HS256
    output_file = None

    for o, a in opts:
        if o in ("-j", "--jwt"):
            jwt_token = a
        elif o in ("-w", "--w"):
            fuzz_file = a
        elif o in ("-k", "--key"):
            secret_key = a
        elif o in ("-a", "--algo"):
            algorithm = a
        elif o in ("-o", "--output"):
            output_file = a

    if not jwt_token or not fuzz_file or not secret_key:
        print('Usage: python3 jwtfuzz.py -j <JWT_PAYLOAD> -w <FUZZ_FILE> -k <SECRET_KEY> -a <ALGO> -o <OUTPUT_FILE>')
        sys.exit(1)

    return jwt_token, fuzz_file, secret_key, algorithm, output_file

if __name__ == '__main__':
    jwt_token, fuzz_file, secret_key, algorithm, output_file = parse_args()
    payload_template = json.loads(jwt_token)
    fuzz_jwt(payload_template, fuzz_file, secret_key, algorithm, output_file)
