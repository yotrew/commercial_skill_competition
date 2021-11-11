Imports System.IO
'VB內建時間操作函數:
'Ref:https://docs.microsoft.com/zh-tw/office/vba/language/reference/user-interface-help/datediff-function
'Ref:https://docs.microsoft.com/zh-tw/office/vba/language/reference/user-interface-help/dateadd-function
Module Module1

    Sub Main()
        Dim sr As StreamReader
        Dim sw As StreamWriter = New StreamWriter("out.txt")
        Dim l As Array = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
        Dim l2 As Array = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
        Dim q, tmp, y, m, d As Integer
        Dim ms, ds As String
        For aa = 1 To 2
            sr = New StreamReader("in" & aa & ".txt")
            q = Val(sr.ReadLine())
            For bb = 1 To q
                y = 1970
                m = 1
                d = 1
                tmp = 1
                tmp += Val(sr.ReadLine())
                While tmp <> 0
                    If y Mod 400 = 0 Then '閏年
                        If tmp >= 366 Then
                            y += 1
                            tmp -= 366
                        Else
                            For x = 1 To l2.Length - 1
                                If l2(x) < tmp Then
                                    tmp -= l2(x)
                                    m += 1
                                Else
                                    d = tmp
                                    tmp = 0
                                    Exit For
                                End If
                            Next
                        End If
                    ElseIf y Mod 100 = 0 Then '非閏年
                        If tmp >= 365 Then
                            y += 1
                            tmp -= 365
                        Else
                            For x = 1 To l.Length - 1
                                If l(x) < tmp Then
                                    tmp -= l(x)
                                    m += 1
                                Else
                                    d = tmp
                                    tmp = 0
                                    Exit For
                                End If
                            Next
                        End If
                    ElseIf y Mod 4 = 0 Then '閏年
                        If tmp >= 366 Then
                            y += 1
                            tmp -= 366
                        Else
                            For x = 1 To l2.Length - 1
                                If l2(x) < tmp Then
                                    tmp -= l2(x)
                                    m += 1
                                Else
                                    d = tmp
                                    tmp = 0
                                    Exit For
                                End If
                            Next
                        End If
                    Else                        '非閏年
                        If tmp >= 365 Then
                            y += 1
                            tmp -= 365
                        Else
                            For x = 1 To l.Length - 1
                                If l(x) < tmp Then
                                    tmp -= l(x)
                                    m += 1
                                Else
                                    d = tmp
                                    tmp = 0
                                    Exit For
                                End If
                            Next
                        End If
                    End If
                End While

                If m < 10 Then
                    ms = 0 & m.ToString()
                Else
                    ms = m.ToString()
                End If
                If d < 10 Then
                    ds = 0 & d.ToString()
                Else
                    ds = d.ToString()
                End If
                sw.WriteLine(y & "-" & ms & "-" & ds)
            Next
            sr.Close()
            If aa = 1 Then
                sw.WriteLine()
            End If
        Next
        sw.Close()
    End Sub

End Module
