```Java
private static String cutIfTooLongText(String plainText) {
    return plainText.length() > 50
      ? plainText.substring(0, 47) + "..."
      : plainText;
  }

  private static String stripHtmlSpaces(String text) {
    if (text == null) {
      return "";
    }

    int cnt = 0;

    for (var ch : text.toCharArray()) {
      // The character 65279 is 'ZERO WIDTH NO-BREAK SPACE' - текст, которого нет
      if ((int) ch == 32 || (int) ch == 65279) {
        cnt++;
      } else {
        break;
      }
    }

    return text.substring(cnt).strip();
```
