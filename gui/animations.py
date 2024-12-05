# gui/animations.py

from PyQt5.QtCore import QPropertyAnimation, QRect


def slide_in(widget, start_rect, end_rect, duration=500):
    """
    Slide a widget into view.
    Args:
        widget: The widget to animate.
        start_rect: Starting position as QRect.
        end_rect: Ending position as QRect.
        duration: Duration of the animation in milliseconds.
    """
    animation = QPropertyAnimation(widget, b"geometry")
    animation.setDuration(duration)
    animation.setStartValue(start_rect)
    animation.setEndValue(end_rect)
    animation.start()
    return animation
