Imports System.IO
Module Module1
    Class student
        Public 座號 As Integer
        Public math As Integer
        Public prog As Integer

    End Class
    Function 排序函數(x As student, y As student)
        If (x.math > y.math) Then
            Return True
        ElseIf (x.math = y.math) Then '數學一樣時比程式
            If (x.prog > y.prog) Then
                Return True
            ElseIf (x.prog = y.prog) Then '程式又一樣時比座號
                If (x.座號 < y.座號) Then
                    Return True
                Else
                    Return False
                End If
            Else
                Return False
            End If
        Else
            Return False
        End If
    End Function
    Sub Main()
        Dim sr1 As StreamReader
        Dim wr1 As StreamWriter = New StreamWriter("out.txt")
        Dim n As Integer
        Dim students As New List(Of student)
        Dim in_str As String()
        For m = 1 To 2
            sr1 = New StreamReader("in" & m & ".txt")
            n = Val(sr1.ReadLine())
            students.Clear()
            For i = 0 To n - 1
                in_str = sr1.ReadLine().Split(" ")
                Dim s As New student
                s.座號 = Val(in_str(0))
                s.math = Val(in_str(1))
                s.prog = Val(in_str(2))
                students.Add(s)
            Next i
            students.Sort(AddressOf 排序函數)
            For x = 0 To n - 1
                wr1.WriteLine(students(x).座號 & " " & students(x).math & " " & students(x).prog)
            Next x
            wr1.WriteLine()
        Next m
        wr1.Close()
    End Sub

End Module
