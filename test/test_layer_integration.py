from src.main import main

def test_main_prints_final_position(capsys):
    # Run main()
    main()
    
    # Capture stdout
    captured = capsys.readouterr()
    assert "0 3 E" in captured.out