  private boolean _jspx_meth_s_005ftext_005f1(javax.servlet.jsp.tagext.JspTag _jspx_th_s_005fif_005f0, PageContext _jspx_page_context)
          throws Throwable {
    PageContext pageContext = _jspx_page_context;
    JspWriter out = _jspx_page_context.getOut();
    //  s:text
    org.apache.struts2.views.jsp.TextTag _jspx_th_s_005ftext_005f1 = (org.apache.struts2.views.jsp.TextTag) _005fjspx_005ftagPool_005fs_005ftext_0026_005fname.get(org.apache.struts2.views.jsp.TextTag.class);
    _jspx_th_s_005ftext_005f1.setPageContext(_jspx_page_context);
    _jspx_th_s_005ftext_005f1.setParent((javax.servlet.jsp.tagext.Tag) _jspx_th_s_005fif_005f0);
    // /WEB-INF/jsps/editor/EntrySidebar.jsp(33,20) name = name type = java.lang.String reqTime = false required = true fragment = false deferredValue = false expectedTypeName = null deferredMethod = false methodSignature = null
    _jspx_th_s_005ftext_005f1.setName("weblogEdit.hasComments");
    int _jspx_eval_s_005ftext_005f1 = _jspx_th_s_005ftext_005f1.doStartTag();
    if (_jspx_eval_s_005ftext_005f1 != javax.servlet.jsp.tagext.Tag.SKIP_BODY) {
      if (_jspx_eval_s_005ftext_005f1 != javax.servlet.jsp.tagext.Tag.EVAL_BODY_INCLUDE) {
        out = _jspx_page_context.pushBody();
        _jspx_th_s_005ftext_005f1.setBodyContent((javax.servlet.jsp.tagext.BodyContent) out);
        _jspx_th_s_005ftext_005f1.doInitBody();
      }
      do {
        out.write("\n");
        out.write("                        ");
        if (_jspx_meth_s_005fparam_005f2(_jspx_th_s_005ftext_005f1, _jspx_page_context))
          return true;
        out.write("\n");
        out.write("                        ");
        if (_jspx_meth_s_005fparam_005f3(_jspx_th_s_005ftext_005f1, _jspx_page_context))
          return true;
        out.write("\n");
        out.write("                    ");
        int evalDoAfterBody = _jspx_th_s_005ftext_005f1.doAfterBody();
        if (evalDoAfterBody != javax.servlet.jsp.tagext.BodyTag.EVAL_BODY_AGAIN)
          break;
      } while (true);
      if (_jspx_eval_s_005ftext_005f1 != javax.servlet.jsp.tagext.Tag.EVAL_BODY_INCLUDE) {
        out = _jspx_page_context.popBody();
      }
    }
    if (_jspx_th_s_005ftext_005f1.doEndTag() == javax.servlet.jsp.tagext.Tag.SKIP_PAGE) {
      _005fjspx_005ftagPool_005fs_005ftext_0026_005fname.reuse(_jspx_th_s_005ftext_005f1);
      return true;
    }
    _005fjspx_005ftagPool_005fs_005ftext_0026_005fname.reuse(_jspx_th_s_005ftext_005f1);
    return false;
  }