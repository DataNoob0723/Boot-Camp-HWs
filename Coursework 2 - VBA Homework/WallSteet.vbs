Sub WallStreet()
    
    Dim sheetsName As Variant

    sheetsName = Array("2016", "2015", "2014")

    For n = 0 To UBound(sheetsName)
        sheet_name = sheetsName(n)
        'MsgBox (sheet_name)

        Worksheets(sheet_name).Range("I1").Value = "Ticker"
        Worksheets(sheet_name).Range("J1").Value = "Yearly Change"
        Worksheets(sheet_name).Range("K1").Value = "Percent Change"
        Worksheets(sheet_name).Range("L1").Value = "Total Stock Volume"

        TotalRows = Worksheets(sheet_name).Rows(Rows.Count).End(xlUp).Row
        Counter = 2

        Dim row_start As Long
        Dim G_Increase As Double
        Dim G_Increase_name As String
        Dim G_Decrease As Double
        Dim G_Decrease_name As String
        Dim G_TVolume As Double
        Dim G_TVolume_name As String
        Dim year As String
        Dim final_date As String
        
        final_date = CStr(Worksheets(sheet_name).Cells(TotalRows, 2).Value)
        'MsgBox (final_date)

        row_start = 2

        G_Increase = 0
        G_Decrease = 0
        G_TVolume = 0

        For i = 2 To TotalRows
            'year = Left(CStr(Worksheets(sheet_name).Cells(i, 2).Value), 4)
            'year = sheet_name
            'final_date = year + "1231"
            If CStr(Worksheets(sheet_name).Cells(i, 2).Value) = final_date Then
                Worksheets(sheet_name).Cells(Counter, 9).Value = Worksheets(sheet_name).Cells(i, 1).Value
                Worksheets(sheet_name).Cells(Counter, 10).Value = Worksheets(sheet_name).Cells(i, 6).Value - Worksheets(sheet_name).Cells(row_start, 3).Value
                ' Check for 0 values
                If Worksheets(sheet_name).Cells(row_start, 3).Value < 0.000001 Then
                    Worksheets(sheet_name).Cells(Counter, 11).Value = (Worksheets(sheet_name).Cells(i, 6).Value - Worksheets(sheet_name).Cells(row_start, 3).Value) / 0.000001
                Else
                    Worksheets(sheet_name).Cells(Counter, 11).Value = (Worksheets(sheet_name).Cells(i, 6).Value - Worksheets(sheet_name).Cells(row_start, 3).Value) / Worksheets(sheet_name).Cells(row_start, 3).Value
                End If

                Worksheets(sheet_name).Cells(Counter, 12).Value = Application.Sum(Range(Worksheets(sheet_name).Cells(row_start, 7), Worksheets(sheet_name).Cells(i, 7)))
                
                If Worksheets(sheet_name).Cells(Counter, 10).Value > 0 Then
                    Worksheets(sheet_name).Cells(Counter, 10).Interior.ColorIndex = 4
                Else
                    Worksheets(sheet_name).Cells(Counter, 10).Interior.ColorIndex = 3
                End If

                If Worksheets(sheet_name).Cells(Counter, 11).Value > G_Increase Then
                    G_Increase = Worksheets(sheet_name).Cells(Counter, 11).Value
                    G_Increase_name = Worksheets(sheet_name).Cells(i, 1).Value
                End If

                If Worksheets(sheet_name).Cells(Counter, 11).Value < G_Decrease Then
                    G_Decrease = Worksheets(sheet_name).Cells(Counter, 11).Value
                    G_Decrease_name = Worksheets(sheet_name).Cells(i, 1).Value
                End If

                If Worksheets(sheet_name).Cells(Counter, 12).Value > G_TVolume Then
                    G_TVolume = Worksheets(sheet_name).Cells(Counter, 12).Value
                    G_TVolume_name = Worksheets(sheet_name).Cells(i, 1).Value
                End If

                Worksheets(sheet_name).Cells(Counter, 11).NumberFormat = "0.00%"

                row_start = i + 1
                Counter = Counter + 1
            End If
        Next i

        Worksheets(sheet_name).Cells(2, 15).Value = "Greatest % Increase"
        Worksheets(sheet_name).Cells(3, 15).Value = "Greatest % Decrease"
        Worksheets(sheet_name).Cells(4, 15).Value = "Greatest Total Volume"

        Worksheets(sheet_name).Cells(1, 16).Value = "Ticker"
        Worksheets(sheet_name).Cells(2, 16).Value = G_Increase_name
        Worksheets(sheet_name).Cells(3, 16).Value = G_Decrease_name
        Worksheets(sheet_name).Cells(4, 16).Value = G_TVolume_name

        Worksheets(sheet_name).Cells(1, 17).Value = "Value"
        Worksheets(sheet_name).Cells(2, 17).Value = G_Increase
        Worksheets(sheet_name).Cells(3, 17).Value = G_Decrease
        Worksheets(sheet_name).Cells(4, 17).Value = G_TVolume

        Worksheets(sheet_name).Cells(2, 17).NumberFormat = "0.00%"
        Worksheets(sheet_name).Cells(3, 17).NumberFormat = "0.00%"
    Next n

           
End Sub