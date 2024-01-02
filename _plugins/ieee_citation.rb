module Jekyll
  module IEEECitationFilter
    require 'citeproc'
    require 'citeproc/ruby'

    def ieee_citation(entry)
        bib = CiteProc::Bibliography.new(entry, :csl)
        bib.render(:bibliography, id: entry, format: 'html', style: 'ieee').html_safe
    end
  end
end

Liquid::Template.register_filter(Jekyll::IEEECitationFilter)
