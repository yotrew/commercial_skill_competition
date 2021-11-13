Imports System
Imports System.Collections.Generic
imports System.Collections
Public Class Test
	Public Shared Sub Main()
		 'Dim chem As HashSet(Of String) = New HashSet(Of String)()
		 'Dim chem As list(Of String) = New list(Of String)() 'ArrayList和List會TLE
		 dim chem as SortedSet(Of Integer) = new SortedSet(Of Integer)
		 dim in1() as String
		 dim i,b as integer
		 console.readline()
		 in1=console.readline().split(" ")
		 'console.writeline(in1.length)
		 
		 for i=0 to in1.length-1
			'b=Integer.parse(in1(i))
			b=in1(i)
			if  not chem.contains(b) then
				chem.add(b)
			end if
		 next
		 console.writeline(chem.count())
	End Sub
End Class