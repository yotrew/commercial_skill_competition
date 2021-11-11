Imports System.IO
Module Module1

    Sub Main()
        Dim sr As StreamReader
        Dim sw As StreamWriter = New StreamWriter("out.txt")
        Dim q As Integer
        For aa = 1 To 2
            sr = New StreamReader("in" & aa & ".txt")
            q = Val(sr.ReadLine())
            For bb = 1 To q
                Dim l As Array
                Dim x1, x2, y1, y2, t As Integer
                l = sr.ReadLine().Split(" ")
                x1 = Integer.Parse(l(0))
                y1 = Integer.Parse(l(1))
                x2 = Integer.Parse(l(2))
                y2 = Integer.Parse(l(3))
                If x1 > x2 Then
                    t = x1
                    x1 = x2
                    x2 = t
                End If
                If y1 > y2 Then
                    t = y1
                    y1 = y2
                    y2 = t
                End If
                If x1 = x2 And y1 = y2 Then
                    sw.WriteLine(0)
                ElseIf x1 = x2 Or y1 = y2 Then
                    sw.WriteLine(1)
                Else
                    If x2 - x1 = y2 - y1 Then
                        sw.WriteLine(1)
                    Else
                        sw.WriteLine(2)
                    End If
                End If
            Next
            If aa = 1 Then
                sw.WriteLine()
            End If
            sr.Close()
        Next
        sw.Close()
    End Sub

End Module
