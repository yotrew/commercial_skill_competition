Imports System.IO
Module Module1

    Sub Main()
        Dim sr As StreamReader
        Dim sw As StreamWriter = New StreamWriter("out.txt")
        Dim q, st, ed, t As Integer
        Dim l As Array
        For aa = 1 To 2
            sr = New StreamReader("in" & aa & ".txt")
            q = Val(sr.ReadLine())
            Dim s1(q - 1), s2(q - 1), s3(q - 1) As Integer
            For bb = 0 To q - 1
                l = sr.ReadLine().Split(" ")
                s1(bb) = Val(l(0))
                s2(bb) = Val(l(1))
                s3(bb) = Val(l(2))
            Next

            Dim s22(q - 1) As Integer
            Array.Copy(s2, s22, q) 's2 複製到 s22 1~q個 index(0~q-1)
            Array.Sort(s2, s1)
            Array.Reverse(s2) : Array.Reverse(s1)
            Array.Sort(s22, s3)
            Array.Reverse(s22) : Array.Reverse(s3)
            ed = 0
            For x = 0 To s3.Length - 1
                For y = 1 To s3.Count - 1
                    st = x
                    If s2(x) = s2(y) Then
                        ed = y
                    ElseIf ed <> 0 Then
                        For z = st To ed - 1
                            For r = z + 1 To ed
                                If s3(z) < s3(r) Then
                                    t = s3(z)
                                    s3(z) = s3(r)
                                    s3(r) = t
                                    t = s1(z)
                                    s1(z) = s1(r)
                                    s1(r) = t
                                ElseIf s3(z) = s3(r) Then  '看座號排序
                                    If s1(z) > s1(r) Then
                                        t = s1(z)
                                        s1(z) = s1(r)
                                        s1(r) = t
                                    End If
                                End If
                            Next
                        Next
                        ed = 0
                    End If
                Next
            Next
            For x = 0 To s1.Length - 1
                sw.WriteLine(s1(x) & " " & s2(x) & " " & s3(x))
            Next
            If aa = 1 Then
                sw.WriteLine()
            End If
            sr.Close()
        Next
        sw.Close()
    End Sub

End Module
