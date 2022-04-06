from play import play


def test_play_returns_message():
    end_messages_list = ['x won!', 'o won!', 'Tie!']
    end_message = play()
    assert end_message in end_messages_list
