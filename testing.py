import helloworld

# if helloworld.my_variable == "hello world":
#     result = True
# else:
#     result = False

# print(result)

def test_hello_world():
    expected_output = "hello world"
    actual_output = helloworld.my_variable  # You can replace this with any other output to intentionally fail
    
    assert actual_output == expected_output


      

