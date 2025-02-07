```
python3 jwtfuzz.py -j '{"iss": "portswigger", "exp": 1738946658, "sub": "FUZZ"}' -w namelist.txt -k 'secret1'                              
admin                eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoiYWRtaW4ifQ.vjj9S9S4Cyw2t9IpreQe4ob9GGUEM8-q1-vLlpMifeM
user1                eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoidXNlcjEifQ.cVRO8ktt6rLtK4WtW8ErvVsvJMzZZm5u_3UA2N3nZO0
user2                eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoidXNlcjIifQ.RIAUYUX3Pw7_rKjotyCSuMIhflBTdjpAATTqrxnsDAk
user3                eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoidXNlcjMifQ.Y6u9FYfzC_Z77MKqFc95fS8CixXbUPYhz_YMNvAotzA
lol4                 eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoibG9sNCJ9.sHPdVHNHjvWuTN86BxgNTjVsBvZ22oSbaMr0E4cKpfE
                                                                                                                                                                                                         
python3 jwtfuzz.py -j '{"iss": "portswigger", "exp": 1738946658, "sub": "FUZZ"}' -w namelist.txt -k 'secret1' -a HS256                     
admin                eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoiYWRtaW4ifQ.vjj9S9S4Cyw2t9IpreQe4ob9GGUEM8-q1-vLlpMifeM
user1                eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoidXNlcjEifQ.cVRO8ktt6rLtK4WtW8ErvVsvJMzZZm5u_3UA2N3nZO0
user2                eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoidXNlcjIifQ.RIAUYUX3Pw7_rKjotyCSuMIhflBTdjpAATTqrxnsDAk
user3                eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoidXNlcjMifQ.Y6u9FYfzC_Z77MKqFc95fS8CixXbUPYhz_YMNvAotzA
lol4                 eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoibG9sNCJ9.sHPdVHNHjvWuTN86BxgNTjVsBvZ22oSbaMr0E4cKpfE
                                                                                                                                                                                                         
python3 jwtfuzz.py -j '{"iss": "portswigger", "exp": 1738946658, "sub": "FUZZ"}' -w namelist.txt -k 'secret1' -a HS256 -o my_jwt_output.txt
admin                eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoiYWRtaW4ifQ.vjj9S9S4Cyw2t9IpreQe4ob9GGUEM8-q1-vLlpMifeM
user1                eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoidXNlcjEifQ.cVRO8ktt6rLtK4WtW8ErvVsvJMzZZm5u_3UA2N3nZO0
user2                eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoidXNlcjIifQ.RIAUYUX3Pw7_rKjotyCSuMIhflBTdjpAATTqrxnsDAk
user3                eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoidXNlcjMifQ.Y6u9FYfzC_Z77MKqFc95fS8CixXbUPYhz_YMNvAotzA
lol4                 eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoibG9sNCJ9.sHPdVHNHjvWuTN86BxgNTjVsBvZ22oSbaMr0E4cKpfE
                                                                                                                                                                                                         
cat my_jwt_output.txt 
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoiYWRtaW4ifQ.vjj9S9S4Cyw2t9IpreQe4ob9GGUEM8-q1-vLlpMifeM
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoidXNlcjEifQ.cVRO8ktt6rLtK4WtW8ErvVsvJMzZZm5u_3UA2N3nZO0
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoidXNlcjIifQ.RIAUYUX3Pw7_rKjotyCSuMIhflBTdjpAATTqrxnsDAk
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoidXNlcjMifQ.Y6u9FYfzC_Z77MKqFc95fS8CixXbUPYhz_YMNvAotzA
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczODk0NjY1OCwic3ViIjoibG9sNCJ9.sHPdVHNHjvWuTN86BxgNTjVsBvZ22oSbaMr0E4cKpfE 
```
