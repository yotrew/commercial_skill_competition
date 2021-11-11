Imports System.IO
Module Module1

    Sub Main()
        Dim sr As StreamReader
        Dim sw As StreamWriter = New StreamWriter("out.txt")
        Dim st, s1, s2, Ans As String
        Dim R As ArrayList = New ArrayList
        Dim l As Array
        Dim q, a, b As Integer
        For x = 1 To 2
            sr = New StreamReader("in" & x & ".txt")
            q = Val(sr.ReadLine())
            For z = 1 To q
                st = sr.ReadLine()
                l = st.Split(" ")
                a = Integer.Parse(l(0))
                b = Integer.Parse(l(1))
                Ans = ""
                s2 = ""
                s1 = Int(a / b).ToString()
                a = a Mod b
                R.Add(a)
                While Len(s2) <> 50 And a <> 0
                    a *= 10
                    s2 &= Int(a / b).ToString()
                    a = a Mod b
                    If R.Contains(a) Then
                        Dim c = R.IndexOf(a) + 1
                        Ans &= Mid(s2, 1, c - 1) & "(" & Mid(s2, c) & ")"
                        Exit While
                    Else
                        R.Add(a)
                    End If
                    If Len(s2) = 50 Then
                        Ans &= "(" & s2 & "...)"
                    End If
                End While
                If Ans = "" Then
                    sw.WriteLine(s1 & "." & s2 & "(0)")
                Else
                    sw.WriteLine(s1 & "." & Ans)
                End If
                R.Clear()
            Next
            sr.Close()
            sw.WriteLine()
        Next
        sw.Close()
    End Sub

End Module
