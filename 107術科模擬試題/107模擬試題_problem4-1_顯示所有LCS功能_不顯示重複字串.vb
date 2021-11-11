Imports System.IO
Module module1
    Dim lcs_str As ArrayList = New ArrayList() '為了方便宣告成全域變數
    'DFS深度優先方式追踨
    Sub lcs(ByRef d(,) As Integer, k As Integer, l As Integer, ByRef str2() As Char, outstr As String)
        If (d(k, l) = 0) Then
            If (Not lcs_str.Contains(outstr)) Then '沒有重複字串就輸出,並加到ArrayList中
                Console.WriteLine(outstr)
                lcs_str.Add(outstr)
            End If

            Return
        End If
        If (d(k, l) = d(k - 1, l - 1) + 1 And d(k, l) <> d(k - 1, l) And d(k, l) <> d(k, l - 1)) Then
            lcs(d, k - 1, l - 1, str2, str2(k - 1) & outstr)
        Else
            If d(k, l) = d(k - 1, l) Then
                lcs(d, k - 1, l, str2, outstr)
            End If
            If d(k, l) = d(k, l - 1) Then
                lcs(d, k, l - 1, str2, outstr)
            End If
        End If
    End Sub
    Sub main()
        Dim sr1 As StreamReader
        Dim wr1 As StreamWriter = New StreamWriter("out.txt")
        Dim n As Integer
        Dim str1 As Char()
        Dim str2 As Char()
        For m = 1 To 2
            sr1 = New StreamReader("in" & m & ".txt")
            n = Val(sr1.ReadLine())

            For i = 0 To n - 1
                str1 = sr1.ReadLine().ToCharArray()
                str2 = sr1.ReadLine().ToCharArray()

                Dim d(str2.Count, str1.Count) As Integer
                'VB初始值為0,所以就不用清空為0
                'For j = 0 To str1.Count
                'd(0, j) = 0
                'Next j
                'For j = 0 To str2.Count
                'd(j, 2) = 0
                'Next j
                For k = 1 To str2.Count
                    For l = 1 To str1.Count
                        If (str2(k - 1) = str1(l - 1)) Then
                            d(k, l) = d(k - 1, l - 1) + 1
                        Else
                            d(k, l) = Math.Max(d(k, l - 1), d(k - 1, l))
                        End If
                    Next l
                Next k

                wr1.WriteLine(d(str2.Count, str1.Count))
                Console.WriteLine("------")
                lcs(d, str2.Count, str1.Count, str2, "") '顯示子字串
                Console.WriteLine("------")
                lcs_str.Clear()
            Next i
            wr1.WriteLine()
        Next m
        wr1.Close()
        Console.ReadLine()
    End Sub

End Module
