def test_hello_world_output(capsys):
    print("hello world")
    captured = capsys.readouterr()  # Capture printed output
    assert captured.out.strip() == "hello world" #this line checks if the captured output matches the expected output
