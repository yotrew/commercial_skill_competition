Module Module1

    Sub Main()
        Dim infile As System.IO.StreamReader
        Dim i, j, k, l, x, y, z, tmp As Integer
        Dim arr_len As Integer
        My.Computer.FileSystem.WriteAllText(".\out.txt", "", False)
        Dim lotte_nums(4) As Integer
        Dim guess_numsX(4) As Integer

        For x = 1 To 2
            infile = My.Computer.FileSystem.OpenTextFileReader(".\in" & x & ".txt")
            arr_len = infile.ReadLine()
            Dim guess_nums(arr_len - 1, 5) As Integer
            Dim data(arr_len) As String
            Dim str_tmp() As String

            For i = 0 To arr_len
                data(i) = infile.ReadLine()
            Next
            str_tmp = Strings.Split(data(0), ",")
            For i = 0 To 4
                lotte_nums(i) = Integer.Parse(str_tmp(i))
            Next
            For i = 1 To arr_len
                str_tmp = Strings.Split(data(i), ",")
                For j = 0 To 5
                    guess_nums(i - 1, j) = Integer.Parse(str_tmp(j))
                Next
            Next

            For i = 1 To arr_len

                Dim times(4) As Integer
                For j = 0 To 5
                    z = 0
                    tmp = 0
                    For k = 0 To 5
                        If k = j Then
                        Else
                            guess_numsX(z) = guess_nums(i - 1, k)
                            z = z + 1
                        End If
                    Next

                    For k = 0 To 4
                        For l = 0 To 4
                            If lotte_nums(k) = guess_numsX(l) Then
                                tmp = tmp + 1
                            End If
                        Next
                    Next
                    If tmp >= 2 Then
                        times(tmp - 2) = times(tmp - 2) + 1
                    End If

                Next
                For k = 0 To 2
                    My.Computer.FileSystem.WriteAllText(".\out.txt", times(k) & ",", True)
                Next
                My.Computer.FileSystem.WriteAllText(".\out.txt", times(3) & vbCrLf, True)
            Next


            My.Computer.FileSystem.WriteAllText(".\out.txt", vbCrLf, True)
        Next
    End Sub

End Module
