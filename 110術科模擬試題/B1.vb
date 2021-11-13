Imports System

Public Class Test
	Public Shared Sub Main()
		dim year as integer
		year=Integer.Parse(console.readline())
		if year mod 400 = 0 then
			console.writeline("a leap year")
		else if year mod 4 = 0 and year mod 100 <> 0 then
			console.writeline("a leap year")
		else
			console.writeline("a normal year")
		end if
	End Sub
End Class