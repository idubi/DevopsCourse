
files_assignment - 
כל תיקייה שיש בתיקייה שהגדרתי כמשתנה
בדיקה אם קיים קובץ טקסט בתיקייה שמתחיל בסימן מסויים ומילה מסויימת. 
אם עמדתי בתנאי -  פרינט לשם של התיקייה. אם הקובץ לא קיים לא עושים כלום.

implementation - 
--> UI --> (react) with file picker and text for pattern 
--> Server --> (python - flask) implement route : 
            @app.route('/check-subfolder-files', methods=['POST'])
			with body : 
			   {
			   path - the directory path to check in
			   file_pattern - regx patter to search files uppon
			   }