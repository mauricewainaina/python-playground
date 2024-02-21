import helloworld

# if helloworld.my_variable == "hello world":
#     result = True
# else:
#     result = False

# print(result)

def test_hello_world():
    expected_output = "hello world"
    actual_output = helloworld.my_variable  # this line checks my variable value from helloworld file
    
    assert actual_output == expected_output  #this assert construct allows you to test asumptions about the code.


      

