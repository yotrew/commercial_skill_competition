Module Module1

    Sub Main()
        Dim infile As System.IO.StreamReader
        Dim i, j, k, l, x, y, z, tmp As Integer
        Dim wi, wj, wk, wm, wn As Integer
        Dim arr_len As Integer
        My.Computer.FileSystem.WriteAllText(".\out.txt", "", False)

        Dim m, r1, r2, n As Integer
        Dim data() As String

        For x = 1 To 2
            infile = My.Computer.FileSystem.OpenTextFileReader(".\in" & x & ".txt")
            arr_len = infile.ReadLine()
            For y = 0 To arr_len - 1
                data = Strings.Split(infile.ReadLine(), ",")
                m = Integer.Parse(data(0))
                r1 = Integer.Parse(data(1))
                r2 = Integer.Parse(data(2))
                n = Integer.Parse(data(3))
                If r1 <> r2 Then
                    My.Computer.FileSystem.WriteAllText(".\out.txt", "無法相乘" & vbCrLf, True)
                Else
                    Dim a_matrix(m - 1, r1 - 1)
                    Dim b_matrix(r2 - 1, n - 1)
                    Dim ab_matrix(m - 1, n - 1)

                    For i = 0 To m - 1
                        data = Strings.Split(infile.ReadLine(), " ")
                        For j = 0 To r1 - 1
                            a_matrix(i, j) = data(j)
                            If data(j) = 9999 Then
                                wi = i
                                wj = j
                                wk = 0
                            End If
                        Next
                    Next

                    For i = 0 To r2 - 1
                        data = Strings.Split(infile.ReadLine(), " ")
                        For j = 0 To n - 1
                            b_matrix(i, j) = data(j)
                            If data(j) = 9999 Then
                                wi = i
                                wj = j
                                wk = 1
                            End If
                        Next
                    Next
                    For i = 0 To m - 1
                        data = Strings.Split(infile.ReadLine(), " ")
                        For j = 0 To n - 1
                            ab_matrix(i, j) = data(j)
                        Next
                    Next

                    If wk = 0 Then
                        For i = 1 To n - 1
                            If b_matrix(wj, i) <> 0 Then
                                wn = i
                                wm = wi
                                Exit For
                            End If
                        Next
                        tmp = ab_matrix(wm, wn)
                        For i = 0 To r1 - 1
                            If i <> wj Then
                                tmp = tmp - a_matrix(wm, i) * b_matrix(i, wn)
                            End If
                        Next
                        tmp = tmp / b_matrix(wj, wn)
                    Else
                        For i = 1 To m - 1
                            If a_matrix(i, wi) <> 0 Then
                                wm = i
                                wn = wj
                                Exit For
                            End If
                        Next
                        tmp = ab_matrix(wm, wn)
                        For i = 0 To r1 - 1
                            If i <> wi Then
                                tmp = tmp - a_matrix(wm, i) * b_matrix(i, wn)
                            End If
                        Next
                        tmp = tmp / a_matrix(wm, wi)
                    End If

                    My.Computer.FileSystem.WriteAllText(".\out.txt", tmp & vbCrLf, True)

                End If
            Next
            My.Computer.FileSystem.WriteAllText(".\out.txt", vbCrLf, True)
            Next
    End Sub

End Module
