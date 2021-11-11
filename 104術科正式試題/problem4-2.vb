Module Module1
    Public Class path
        Public x As String
        Public y As String
        Public weight As Integer
    End Class
    Sub Main()
        Dim infile As System.IO.TextReader
        Dim i, j, k, l, x, y, z As Integer
        Dim datasets_len As Integer
        Dim rawdata() As String
        Dim pathdata() As String

        My.Computer.FileSystem.WriteAllText(".\out.txt", "", False)


        For x = 1 To 2
            infile = My.Computer.FileSystem.OpenTextFileReader(".\in" & x & ".txt")
            datasets_len = infile.ReadLine()
            For i = 0 To datasets_len - 1
                rawdata = Strings.Split(infile.ReadLine(), " ")
                Dim Graphs(rawdata.Length - 1) As path
                Dim MST(rawdata.Length - 1) As path '為了快,就不處理n-1(n is number of verterx)
                Dim Q(rawdata.Length - 1) As String
                Dim Q_Len As Integer = 0
                Dim Q_Top As Integer = 0
                For j = 0 To rawdata.Length - 1
                    pathdata = Strings.Split(rawdata(j), ",")
                    Dim tmp_path As New path
                    tmp_path.x = pathdata(0)
                    tmp_path.y = pathdata(1)
                    tmp_path.weight = pathdata(2)
                    Graphs(j) = tmp_path
                Next
                sort_path(Graphs)
                Dim MST_len As Integer = 0
                Dim cycle As Boolean = False
                Dim weight As Integer = 0
                Dim next_vertex As String = ""


                For j = 0 To Graphs.Length - 1

                    'start:判斷有沒有cycle
                    cycle = False
                    Q_Len = 1
                    Q_Top = 0
                    Q(Q_Top) = Graphs(j).x
                    While (Q_Top < Q_Len)
                        next_vertex = ""
                        For k = 0 To MST_len - 1
                            If Q(Q_Top) = MST(k).x Then
                                next_vertex = MST(k).y
                            End If
                            If Q(Q_Top) = MST(k).y Then
                                next_vertex = MST(k).x
                            End If
                            For l = 0 To Q_Len - 1
                                If next_vertex = Q(l) Then
                                    Exit For
                                End If
                            Next
                            If l >= Q_Len And next_vertex <> "" Then
                                Q(Q_Len) = next_vertex
                                Q_Len = Q_Len + 1
                            End If
                        Next
                        For l = 0 To Q_Len - 1
                            If Graphs(j).y = Q(l) Then
                                Q_Top = Q_Len
                                cycle = True
                            End If
                        Next
                        Q_Top = Q_Top + 1
                    End While
                    'end:判斷有沒有cycle



                    If Not cycle Then
                        Dim tmp_path As New path
                        tmp_path.x = Graphs(j).x
                        tmp_path.y = Graphs(j).y
                        tmp_path.weight = Graphs(j).weight
                        weight = weight + Graphs(j).weight
                        MST(MST_len) = tmp_path
                        MST_len = MST_len + 1
                    End If
                Next

                My.Computer.FileSystem.WriteAllText(".\out.txt", weight & vbCrLf, True)
            Next
            My.Computer.FileSystem.WriteAllText(".\out.txt", vbCrLf, True)
        Next
    End Sub

    Sub sort_path(ByVal paths() As path)
        Dim i, j As Integer
        For i = 0 To paths.Length - 1
            For j = i + 1 To paths.Length - 1
                If paths(i).weight > paths(j).weight Then
                    swap_path(paths(i), paths(j))
                End If
            Next
        Next
    End Sub
    Sub swap_path(ByVal a As path, ByVal b As path)
        Dim c As New path
        c.x = a.x
        c.y = a.y
        c.weight = a.weight
        a.x = b.x
        a.y = b.y
        a.weight = b.weight
        b.x = c.x
        b.y = c.y
        b.weight = c.weight
    End Sub

End Module
