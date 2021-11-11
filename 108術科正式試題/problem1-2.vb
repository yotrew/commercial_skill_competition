Imports System.IO
Module Module1

    Sub Main()
        Dim sr As StreamReader
        Dim sw As StreamWriter = New StreamWriter("out.txt")

        Dim ans As ArrayList = New ArrayList
        Dim grade As ArrayList = New ArrayList
        Dim q, sum, c, t, ed As Integer
        Dim str As String
        For xx = 1 To 2
            sr = New StreamReader("in" & xx & ".txt")
            q = Val(sr.ReadLine())
            For x = 1 To q
                Dim l As Array
                str = sr.ReadLine()
                l = str.Split(" ")
                For y = 0 To l.Length - 1
                    If IsNumeric(l(y)) Then
                        ans.Add(Val(l(y)))
                    ElseIf l(y) = "X" Then
                        ans.Add(-10)
                    ElseIf l(y) = "/" Then
                        ans.Add(ans(y - 1) - 10)
                    End If
                Next
                c = 0
                sum = 0
                t = 0
                For y = 0 To ans.Count - 1
                    If ans(y) >= 0 Then
                        sum += ans(y)
                        c += 1
                        t += 1
                    ElseIf ans(y) < 0 And ans(y) <> -10 Then
                        sum += Math.Abs(ans(y)) + Math.Abs(ans(y + 1))
                        c += 1
                        t += 1
                    ElseIf ans(y) = -10 Then
                        sum += Math.Abs(ans(y)) + Math.Abs(ans(y + 1)) + Math.Abs(ans(y + 2))
                        c += 2
                        t += 2
                    End If
                    If c = 2 Then
                        grade.Add(sum)
                        sum = 0
                        c = 0
                        If t = 18 Then
                            t = y + 1
                            Exit For
                        End If
                    End If
                Next
                For y = t To ans.Count - 1
                    sum += Math.Abs(ans(y))
                Next
                grade.Add(sum)

                ed = 0
                For y = 0 To grade.Count - 1
                    ed += grade(y)
                Next
                sw.WriteLine(ed)
                ans.Clear()
                grade.Clear()
            Next
            sw.WriteLine()
            sr.Close()
        Next
        sw.Close()
    End Sub

End Module
