Imports System.IO
Module Module1
    Function mattio(n)
        Dim a(1501), b(1501), c(1501) As Integer
        Dim s As Long
        a(0) = 0
        b(0) = 1
        For i = 1 To n - 1
            For j = 0 To 1500
                c(j) = c(j) + (a(j) + b(j)) Mod 1000
                c(j + 1) = (a(j) + b(j)) \ 1000
            Next

            b.CopyTo(a, 0)
            c.CopyTo(b, 0)

        Next

        '找到第1位數字不是0的地方
        Dim x = 1501
        For i = 1501 To 0 Step -1
            If (b(i) > 0) Then
                x = i
                Exit For
            End If
        Next

        For i = x To 0 Step -1
            s &= b(i).ToString().Trim(" ")
        Next
        mattio = s
    End Function
    Sub Main()
        Dim sr As StreamReader
        Dim sw As StreamWriter = New StreamWriter("out.txt")
        Dim q As Integer
        For aa = 1 To 2
            sr = New StreamReader("in" & aa & ".txt")
            q = Val(sr.ReadLine())
            For bb = 1 To q
                Dim c As Integer
                c = Val(sr.ReadLine())
                sw.Write(mattio(c))
            Next
            If aa = 1 Then
                sw.WriteLine()
            End If
            sr.Close()
        Next
        sw.Close()
    End Sub

End Module
