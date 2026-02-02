---
title: "AI-ISL - Publications"
layout: gridlay
excerpt: "Publications."
sitemap: false
permalink: /publications/
---


# Publications
Jump to 
[preprints](#preprints),
[conference papers](#peer-reviewed-conference),
 [workshop papers](#peer-reviewed-workshop),
 [journal papers](#peer-reviewed-journal),
 [patents](#patents), [thesis](#thesis).


<!-- ## Highlights

{% for publi in site.data.publist %}
{% if publi.highlight == 1 %}

  **<a href="{{ publi.link }}">{{ publi.title }}</a>** <br />
  {{ publi.authors }} <br />
  {{ publi.venue }}

{% endif %}
{% endfor %} -->


<p> &nbsp; </p>

## Preprints

{% for publi in site.data.publist %}
{% if publi.published == 0 %}

  **<a href="{{ publi.link }}">{{ publi.title }}</a>** <br />
  {{ publi.authors }}<br />
  {{ publi.venue }}

{% endif %}
{% endfor %}


## Peer-reviewed Conference

{% for publi in site.data.publist %}
{% if publi.cwj_code == 0 %}
{% if publi.published == 1 %}

  **<a href="{{ publi.link }}">{{ publi.title }}</a>** <br />
  {{ publi.authors }} <br />
  {{ publi.venue }}

{% endif %}
{% endif %}
{% endfor %}


## Peer-reviewed Workshop

{% for publi in site.data.publist %}
{% if publi.cwj_code == 1 %}
{% if publi.published == 1 %}

  **<a href="{{ publi.link }}">{{ publi.title }}</a>** <br />
  {{ publi.authors }} <br />
  {{ publi.venue }}

{% endif %}
{% endif %}
{% endfor %}


## Peer-reviewed Journal

{% for publi in site.data.publist %}
{% if publi.cwj_code == 2 %}
{% if publi.published == 1 %}

  **<a href="{{ publi.link }}">{{ publi.title }}</a>** <br />
  {{ publi.authors }} <br />
  {{ publi.venue }}

{% endif %}
{% endif %}
{% endfor %}

## Patents
**DNA 저장 장치의 연성 정보 기반 복호화 방법, 프로그램 및 장치** <br />
Sunghwan Kim, Hosung Park, Albert No, Jae-Won Kim, Jaeho Jeong, and Jong-Seon No <br /> 
Korean Patent (KR 10-2339723), December 2021

**데이터 압축 및 압축해제방법** <br />
 Albert No <br /> 
Korean Patent (KR 10-2016125 B1), August 2019


## Thesis
**<a href="https://searchworks.stanford.edu/view/11391861">Rateless Lossy Compression via the Extremes</a>** <br />
PhD Thesis, Stanford University, 2015 <br />
Advisor: Tsachy Weissman
