# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class StudentGrades(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, grade: str=None):  # noqa: E501
        """StudentGrades - a model defined in Swagger

        :param grade: The grade of this StudentGrades.  # noqa: E501
        :type grade: str
        """
        self.swagger_types = {
            'grade': str
        }

        self.attribute_map = {
            'grade': 'grade'
        }

        self._grade = grade

    @classmethod
    def from_dict(cls, dikt) -> 'StudentGrades':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Student_grades of this StudentGrades.  # noqa: E501
        :rtype: StudentGrades
        """
        return util.deserialize_model(dikt, cls)

    @property
    def grade(self) -> str:
        """Gets the grade of this StudentGrades.


        :return: The grade of this StudentGrades.
        :rtype: str
        """
        return self._grade

    @grade.setter
    def grade(self, grade: str):
        """Sets the grade of this StudentGrades.


        :param grade: The grade of this StudentGrades.
        :type grade: str
        """

        self._grade = grade
