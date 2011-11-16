from Products.CMFCore.utils import getToolByName

def import_various(context):
    
    if not context.readDataFile('medialog.subskins_various.txt'):
        return
        
    site = context.getSite()
    kupu = getToolByName(site, 'kupu_library_tool')
    
    paragraph_styles = list(kupu.getParagraphStyles())
    
    new_styles = [('times', 'times|span'),
                  ('verdana', 'verdana|span'),
                  ('lucida', 'lucida|span'),
                  ('helvetica', 'helvetica|span'),
                  ('color1', 'color1|span'),
                  ('color2', 'color2|span'),
                  ('color3', 'color3|span'),
                  ('color4', 'color4|span'),
                  ('color5', 'color5|span'),
                  ('color5', 'color6|span'),
                  ('black', 'black|span')]
    to_add = dict(new_styles)
    
    for style in paragraph_styles:
        css_class = style.split('|')[-1]
        if css_class in to_add:
            del to_add[css_class]

    if to_add:
        paragraph_styles += ['%s|%s' % (v, k) for k,v in new_styles if k in to_add]
        kupu.configure_kupu(parastyles=paragraph_styles)