"""Excel writer module for generating formatted Excel output."""

import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from .config import Config


class ExcelWriter:
    """Handles Excel file generation with proper formatting."""
    
    def __init__(self, filename=None):
        """
        Initialize the Excel writer.
        
        Args:
            filename: Output filename (default: from Config)
        """
        self.filename = filename or Config.DEFAULT_OUTPUT_FILENAME
    
    def write_data(self, data, sheet_name='Market Analysis'):
        """
        Write data to Excel file with formatting.
        
        Args:
            data: List of dictionaries containing app data
            sheet_name: Name of the Excel sheet
            
        Returns:
            Path to the created Excel file
        """
        # Create DataFrame
        df = pd.DataFrame(data, columns=Config.EXCEL_COLUMNS)
        
        # Write to Excel using pandas with xlsxwriter engine
        with pd.ExcelWriter(self.filename, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            
            # Get workbook and worksheet objects
            workbook = writer.book
            worksheet = writer.sheets[sheet_name]
            
            # Define formats
            header_format = workbook.add_format(Config.EXCEL_HEADER_FORMAT)
            cell_format = workbook.add_format(Config.EXCEL_CELL_FORMAT)
            link_format = workbook.add_format({
                'font_color': '#0563C1',
                'underline': True,
                'border': 1,
                'align': 'left',
                'valign': 'vcenter'
            })
            
            # Write headers with formatting
            for col_num, column in enumerate(Config.EXCEL_COLUMNS):
                worksheet.write(0, col_num, column, header_format)
            
            # Set column widths
            for col_num, column in enumerate(Config.EXCEL_COLUMNS):
                width = Config.COLUMN_WIDTHS.get(column, 15)
                worksheet.set_column(col_num, col_num, width)
            
            # Format data cells and make links clickable
            for row_num, row_data in enumerate(data, start=1):
                for col_num, column in enumerate(Config.EXCEL_COLUMNS):
                    value = row_data.get(column, '')
                    
                    # Handle link columns
                    if 'Link' in column or column == 'Website':
                        if value and value != 'N/A':
                            # Write as hyperlink
                            worksheet.write_url(row_num, col_num, value, link_format, string=value)
                        else:
                            worksheet.write(row_num, col_num, value, cell_format)
                    else:
                        worksheet.write(row_num, col_num, value, cell_format)
            
            # Freeze top row
            worksheet.freeze_panes(1, 0)
        
        return self.filename
    
    def write_multiple_sheets(self, data_dict):
        """
        Write multiple sheets to Excel file.
        
        Args:
            data_dict: Dictionary where keys are sheet names and values are data lists
            
        Returns:
            Path to the created Excel file
        """
        with pd.ExcelWriter(self.filename, engine='xlsxwriter') as writer:
            for sheet_name, data in data_dict.items():
                # Sanitize sheet name - Excel doesn't allow certain characters
                sanitized_name = sheet_name.replace('/', '-').replace('\\', '-').replace('[', '').replace(']', '').replace('*', '').replace('?', '').replace(':', '')
                # Limit to 31 characters (Excel limit)
                sanitized_name = sanitized_name[:31]
                
                df = pd.DataFrame(data, columns=Config.EXCEL_COLUMNS)
                df.to_excel(writer, sheet_name=sanitized_name, index=False)
                
                # Get workbook and worksheet objects
                workbook = writer.book
                worksheet = writer.sheets[sanitized_name]
                
                # Define formats
                header_format = workbook.add_format(Config.EXCEL_HEADER_FORMAT)
                cell_format = workbook.add_format(Config.EXCEL_CELL_FORMAT)
                link_format = workbook.add_format({
                    'font_color': '#0563C1',
                    'underline': True,
                    'border': 1,
                    'align': 'left',
                    'valign': 'vcenter'
                })
                
                # Write headers with formatting
                for col_num, column in enumerate(Config.EXCEL_COLUMNS):
                    worksheet.write(0, col_num, column, header_format)
                
                # Set column widths
                for col_num, column in enumerate(Config.EXCEL_COLUMNS):
                    width = Config.COLUMN_WIDTHS.get(column, 15)
                    worksheet.set_column(col_num, col_num, width)
                
                # Format data cells and make links clickable
                for row_num, row_data in enumerate(data, start=1):
                    for col_num, column in enumerate(Config.EXCEL_COLUMNS):
                        value = row_data.get(column, '')
                        
                        # Handle link columns
                        if 'Link' in column or column == 'Website':
                            if value and value != 'N/A':
                                # Write as hyperlink
                                worksheet.write_url(row_num, col_num, value, link_format, string=value)
                            else:
                                worksheet.write(row_num, col_num, value, cell_format)
                        else:
                            worksheet.write(row_num, col_num, value, cell_format)
                
                # Freeze top row
                worksheet.freeze_panes(1, 0)
        
        return self.filename
