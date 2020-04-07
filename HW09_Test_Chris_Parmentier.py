#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on April 1 2020 

@author: Chris Parmentier 
The purpose of this file is to call the unittest and test HW09 :)

"""

import unittest
from typing import Dict 


from HW09_Chris_Parmentier import Student, Instructor, Repository 

class student_test(unittest.TestCase):
    "goal of this class is to test student"
    def test_student(self) -> None:
        "we'll take the student class through each of the defined functions  "
        e = Student('0002','Bellwoar, Emily', 'Teaching')        
        e.store_course_grade('TESOL501','A++++') # we take the course only.... until next week!
        expected : Dict[str, str, str, Dict] = ['0002', 'Bellwoar, Emily', 'Teaching', ['TESOL501']]
        self.assertEqual(e.info(),expected)
        
class instructor_test(unittest.TestCase):
    "goal of this class is to test instructor"
    def test_instructor(self) -> None:
        "we'll take the instructor class through each of the defined functions  "
        t = Instructor('0001','Stevens, Edwin Augustus', 'Education')        
        t.store_course_student('HIST101')
        expected  : Dict[str, str, str, Dict[str,int]]=['0001', 'Stevens, Edwin Augustus', 'Education', 'HIST101', 1]
        self.assertEqual(t.info(), expected)
    
class repository_test(unittest.TestCase):
    #goal of this class is to test repository
    def test_repository(self) -> None:
        #we'll take the repository class through each of the defined functions  
        r: Repository = Repository("/Users/Christopher/Desktop/SSW810/Test")

        self.assertEqual(r.students,['0001', 'Parmentier', 'Mechanical', 'SSW 567'])   # this isn't working I think I need to print out the object of student differently        
        self.assertEqual(r.instructors, ['0002', 'Bellwoar,E ', 'SFEN', 'SSW 567', 1]) # same with this test
  
    
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)            
                
      

                    
