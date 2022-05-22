function domainName(url) {
   if (url.startsWith("http://")) {
      url = url.replace("http://", "");
      if (url.startsWith("www.")) {
         url = url.replace("www.", "");
      }
   } else if (url.startsWith("https://")) {
      url = url.replace("https://", "");
      if (url.startsWith("www.")) {
         url = url.replace("www.", "");
      }
   } else if (url.startsWith("www.")) {
      url = url.replace("www.", "");
   }
   return url.split(".")[0];
}
