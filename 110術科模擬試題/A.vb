Imports System

Public Class Test
	Public Shared Sub Main()
		dim a,b,c,n as integer
		Dim in1() as String
		While True
			try
				in1=split(console.readline()," ")
				a=Integer.Parse(in1(0))
				b=Integer.Parse(in1(1))
				c=Integer.Parse(in1(2))
				console.writeline(24*a+14*b+6*c)
			catch ex As Exception
				exit while
			end try
		End while
	End Sub
End Class