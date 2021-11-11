Imports System.IO
Module Module1

    Sub Main()
        Dim sr As StreamReader
        Dim sw As StreamWriter = New StreamWriter("out.txt")
        Dim q As Integer
        For aa = 1 To 2
            sr = New StreamReader("in" & aa & ".txt")
            q = Val(sr.ReadLine())
            Dim sn(q - 1), sm(q - 1), sp(q - 1), sum(q - 1) As Integer
            Dim copy(q - 1) As Integer
            Dim copy2(q - 1) As Integer
            For bb = 0 To q - 1
                Dim l As Array
                l = sr.ReadLine().Split(" ")
                sn(bb) = Integer.Parse(l(0))
                sm(bb) = Integer.Parse(l(1))
                sp(bb) = Integer.Parse(l(2))
                sum(bb) = Integer.Parse(l(1)) * 1000 + Integer.Parse(l(2)) * 100 + (50 - Integer.Parse(l(0)))
            Next
            sum.CopyTo(copy, 0)
            sum.CopyTo(copy2, 0)
            Array.Sort(sum, sn)
            Array.Sort(copy, sm)
            Array.Sort(copy2, sp)
            Array.Reverse(sn) : Array.Reverse(sm) : Array.Reverse(sp)

            For x = 0 To sn.Length - 1
                sw.WriteLine(sn(x) & " " & sm(x) & " " & sp(x))
            Next


            If aa = 1 Then
                sw.WriteLine()
            End If
            sr.Close()
        Next
        sw.Close()
    End Sub

End Module
