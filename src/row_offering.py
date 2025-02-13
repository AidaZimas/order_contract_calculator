class RowForOffering:
    def __init__(self, off_row_text, off_row_value, off_row_is_additional_text):
        self.off_row_text = off_row_text
        self.off_row_value = off_row_value
        self.off_row_is_additional_text = off_row_is_additional_text

    def __repr__(self):
        return f"text='{self.off_row_text}', value='{self.off_row_value}')"