# PageSetup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | [**Link**](Link.md) |  | [optional] 
**black_and_white** | **bool** | Represents if elements of the document will be printed in black and white. True/False | [optional] 
**bottom_margin** | **float** | Represents the size of the bottom margin, in unit of centimeters. | [optional] 
**center_horizontally** | **bool** | Represent if the sheet is printed centered horizontally. | [optional] 
**center_vertically** | **bool** | Represent if the sheet is printed centered vertically. | [optional] 
**first_page_number** | **int** | Represents the first page number that will be used when this sheet is printed. | [optional] 
**fit_to_pages_tall** | **int** | Represents the number of pages tall the worksheet will be scaled to when it&#39;s printed. | [optional] 
**fit_to_pages_wide** | **int** | Represents the number of pages wide the worksheet will be scaled to when it&#39;s printed. | [optional] 
**footer_margin** | **float** | Represents the distance from the bottom of the page to the footer, in unit of centimeters. | [optional] 
**header_margin** | **float** | Represents the distance from the top of the page to the header, in unit of centimeters. | [optional] 
**is_auto_first_page_number** | **bool** | Indicates whether the first the page number is automatically assigned. | [optional] 
**is_hf_align_margins** | **bool** | Indicates whether header and footer margins are aligned with the page margins.Only applies for Excel 2007. | [optional] 
**is_hf_diff_first** | **bool** | True means that the header/footer of the first page is different with other pages. | [optional] 
**is_hf_diff_odd_even** | **bool** | True means that the header/footer of the odd pages is different with odd pages. | [optional] 
**is_hf_scale_with_doc** | **bool** | Indicates whether header and footer are scaled with document scaling.Only applies for Excel 2007.  | [optional] 
**is_percent_scale** | **bool** | If this property is False, the FitToPagesWide and FitToPagesTall properties control how the worksheet is scaled. | [optional] 
**left_margin** | **float** | Represents the size of the left margin, in unit of centimeters. | [optional] 
**order** | **str** | Represents the order that Microsoft Excel uses to number pages when printing a large worksheet. | [optional] 
**orientation** | **str** | Represents page print orientation. | [optional] 
**paper_size** | **str** | Represents the size of the paper. | [optional] 
**print_area** | **str** | Represents the range to be printed. | [optional] 
**print_comments** | **str** | Represents the way comments are printed with the sheet. | [optional] 
**print_copies** | **int** | Get and sets number of copies to print. | [optional] 
**print_draft** | **bool** | Represents if the sheet will be printed without graphics. | [optional] 
**print_errors** | **str** | Specifies the type of print error displayed. | [optional] 
**print_gridlines** | **bool** | Represents if cell gridlines are printed on the page. | [optional] 
**print_headings** | **bool** | Represents if row and column headings are printed with this page. | [optional] 
**print_quality** | **int** | Represents the print quality. | [optional] 
**print_title_columns** | **str** | Represents the columns that contain the cells to be repeated on the left side of each page. | [optional] 
**print_title_rows** | **str** | Represents the rows that contain the cells to be repeated at the top of each page. | [optional] 
**right_margin** | **float** | Represents the size of the right margin, in unit of centimeters. | [optional] 
**top_margin** | **float** | Represents the size of the top margin, in unit of centimeters. | [optional] 
**zoom** | **int** | Represents the scaling factor in percent. It should be between 10 and 400. | [optional] 
**header** | [**list[PageSection]**](PageSection.md) | Represents the page header. | [optional] 
**footer** | [**list[PageSection]**](PageSection.md) | Represents the page footor. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

