
/* Problem
	Given N integers, count the total pairs of integers that have a difference of K.

	Input Format 
	1st line contains N & K (integers).
	2nd line contains N numbers of the set. All the N numbers are assured to be distinct.

	Output Format	
	One integer saying the number of pairs of numbers that have a diff K.

	Constraints:
	N <= 10^5
	0 < K < 10^9
	Each integer will be greater than 0 and at least K away from 2^31-1
*/

using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    
   // A class which stores a students score and the amount of candies that they have
   public class Student
   {
       public int score = 0;
       public int candies = 0;
   }
    
    static void Main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution */
        
        int numberOfStudents = int.Parse( Console.ReadLine() );
         
         // Create a list to store all students and a variable to store last student procesed
        List<Student> listOfStudents = new List<Student>();
        var lastStudent = new Student();

        // Store the amount of candies to award the student 
        int candyAwarded = 1; 
        
        for ( int i = 0; i < numberOfStudents; i++ )
        {
           Student newStudent = CreateStudent( int.Parse( Console.ReadLine() ));
           

           if ( newStudent.score > lastStudent.score )
           {
                   newStudent.candies = candyAwarded;
                   candyAwarded++;
                   listOfStudents.Add( newStudent );
                   lastStudent = newStudent;
           }
           else if ( newStudent.score < lastStudent.score )
           {
               candyAwarded = 1;
               newStudent.candies = candyAwarded;
               UpdateLeft( ref listOfStudents , newStudent);
               listOfStudents.Add( newStudent);
               candyAwarded++;
               lastStudent = newStudent;
           }
           else 
           {
            
               candyAwarded = 1;
               newStudent.candies = candyAwarded;
               listOfStudents.Add( newStudent );
               lastStudent = newStudent;
               candyAwarded++;
           }
        }
        int count = 0;
        
        foreach ( var stud in listOfStudents)
        {
            count += stud.candies;
        }
        Console.WriteLine( count);
     
    }  

    public static Student CreateStudent( int score )
    {
        Student tmpStud = new Student();
        tmpStud.score = score;
        return tmpStud;
    }
    
    public static void  UpdateLeft( ref List<Student> listOfStudents , Student next )
    {
        if ( listOfStudents.Count <= 1)
        {
            if ( listOfStudents[0].score > next.score)
                listOfStudents[0].candies++;
            
            return;
        }
        int endOfList = listOfStudents.Count -1;
        
        for ( int i = endOfList; i >= 1; i--)
        {
            
            if ( listOfStudents[i - 1].score > listOfStudents[i].score)
            {
                listOfStudents[i].candies++;
            }
            
            
            if ( listOfStudents[i -1 ].score == listOfStudents[i].score )
            {
                  listOfStudents[i].candies++;
                  return;
            }
            
            if ( listOfStudents[i -1 ].score <= listOfStudents[i].score)
            {
                if ( i == endOfList)
                {
                    return;
                }
                if ( listOfStudents[i].candies <= listOfStudents[i + 1].candies )
                {
                    listOfStudents[i].candies = listOfStudents[i + 1].candies + 1;
                }           
                return;
            }
        }
        
        
        if ( listOfStudents[0].score > listOfStudents[1].score)
        {
            listOfStudents[0].candies = listOfStudents[1].candies + 1;
        }
        
        return;
        
        
    }
 
}