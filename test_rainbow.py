import rainbow

def test_main():
    assert rainbow.main(1000)

def test_ansi_type():
    assert rainbow.ansi_color_test()

#test_main()