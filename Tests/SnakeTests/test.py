import pygame
import sys
import pytest
import random
from pygame.locals import *


def test_game_over():
    with pytest.raises(SystemExit) as wrapped_exception:
        game_over()
    assert wrapped_exception.type == SystemExit


def test_show_score():
    score = 10
    color = (255, 255, 255)
    font = 'consolas'
    size = 20
    show_score(0, color, font, size)
    show_score(1, color, font, size)


@pytest.mark.parametrize("direction, change_to, expected_direction", [
    ('UP', 'DOWN', 'DOWN'),
    ('DOWN', 'UP', 'UP'),
    ('LEFT', 'RIGHT', 'RIGHT'),
    ('RIGHT', 'LEFT', 'LEFT'),
])
def test_direction_change(direction, change_to, expected_direction):
    assert direction == expected_direction


def test_game_logic():
    snake_pos = [50, 50]
    snake_body = [[50, 50], [40, 50], [30, 50]]
    food_pos = [60, 50]
    food_spawn = True
    direction = 'RIGHT'
    change_to = 'RIGHT'
    score = 0

    game_logic()

    assert len(snake_body) == 3
    assert snake_body[0] == [60, 50]
    assert score == 1
