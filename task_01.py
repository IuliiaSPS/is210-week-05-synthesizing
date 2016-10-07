#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01"""

import datetime

CURDATE = None

if __name__ == '__main__':
    CURDATE = datetime.date.today()


def get_current_date():
    """This function uses imported module datetime to return current date.

        Args:
            Does not take any parameters.

        Returns:
            String datetime.date and current date.

        Examples:
            >>> task_01.get_current_date()
            datetime.date(2016, 10, 7)
    """
    return datetime.date.today()
