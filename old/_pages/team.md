---
title: "AI-ISL - Team"
layout: gridlay
excerpt: "Team"
sitemap: false
permalink: /team/
---

<p> &nbsp;</p>
# Group Members

## Professor
<div class="row">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/albert_230824.jpg" class="img-responsive" width="25%" style="float: left" />
<h3>Albert No (노승문) </h3>
Associate Professor <br />
Department of Artificial Intelligence<br />
Yonsei University, Engineering Research Park (공학원) Room 449D, 50 Yonsei-ro, Seodaemun-gu, Seoul <br />
albertno AT yonsei DOT ac DOT kr<br />
<h4> Education </h4>
  <ul style="overflow: hidden">
<li> PhD, Department of Electrical Engineering, Stanford University, 2015</li>
<li> Ms, Department of Electrical Engineering, Stanford University, 2012</li>
<li> Bs, Department of Electrical Engineering and Department of Mathematical Science (Double Major),
Seoul National University, 2009 </li>
</ul>
<h4> Work Experience </h4>
  <ul style="overflow: hidden">
<li> Associate Professor, Yonsei University, 2024.03 - </li>
<li> Associate Professor, Hongik University, 2023.03 - 2024.02 </li>
<li> Assistant Professor, Hongik University, 2017.03 -2023.02 </li>
<li> Principal Scientist, Roche Sequencing Solutions, 2015.11 - 2017.02</li>
</ul>
</div>


<p> &nbsp; </p>


## PhD Candidates
{% for s in site.data.students %}
{% if s.ump == 2 %}

<div class="row">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ s.fname }}" class="img-responsive" width="25%" style="float: left" />
<h3>
  {% if s.link %}
    <a href="{{ s.link }}" target="_blank">{{ s.name }}</a>
  {% else %}
    {{ s.name }}
  {% endif %}
</h3>
<h4>PhD Candidate </h4>
{{ s.email | replace: "@", " [at] " | replace: ".", " [dot] " }}<br />
Research Interest: {{ s.desc }}
</div>

{% endif %}
{% endfor %}

<p> &nbsp; </p>

## MS Candidates
{% for s in site.data.students %}
{% if s.ump == 1 %}

<div class="row">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ s.fname }}" class="img-responsive" width="25%" style="float: left" />
<h3>
  {% if s.link %}
    <a href="{{ s.link }}" target="_blank">{{ s.name }}</a>
  {% else %}
    {{ s.name }}
  {% endif %}
</h3>
<h4>MS Candidate </h4>
{{ s.email | replace: "@", " [at] " | replace: ".", " [dot] " }}<br />
Research Interest: {{ s.desc }}
</div>

{% endif %}
{% endfor %}

<p> &nbsp; </p>


<!-- ## BS Interns
{% for s in site.data.students %}
{% if s.ump == 0 %}

<div class="row">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ s.fname }}" class="img-responsive" width="25%" style="float: left" />
<h3>{{ s.name }}</h3>
<h4>Undergraduate Intern </h4>
<a href="mailto:{{ s.email }}">{{ s.email }}</a><br />
Research Interest: {{ s.desc }}
</div>

{% endif %}
{% endfor %}

<p> &nbsp; </p> -->

## Alumni
  <ul style="overflow: hidden">
<li> Halyn Yu (유하린, Hongik University, MS '25) </li>
<li> Beom Soo Lee (이범수, Hongik University, MS '25)  </li>
<li> Junseok Jang (장준석, Hongik University, undergrad intern)  </li>
<li> JiHyun Jung (정지현, Hongik University, undergrad intern), currently at Virginia Tech (Master Program)  </li>
<li> Ki-wook Hong (홍기욱, Hongik University, undergrad intern)  </li>
<li> Dayeon Kim (김다연, Hongik University, undergrad intern)  </li>
<li> Beomseok Seo (서범석, Hongik University, undergrad intern)  </li>
<li> Yebin Wang (왕예빈, Hongik University, MS '24)  </li>
<li> Sanghoon Kang (강상훈, Hongik University, PhD '23), currently at University of Florida (Postdoctoral Associate) </li>
<li> Yunfei Gao (고운비, Hongik University, MS '19, PhD '23), currently at Shanghai Jiao Tong University (Postdoctoral Associate) </li>
<li> Minhyeok Cho (조민혁, Hongik University, MS '23), currently at FuriosaAI </li>
<li> Jinhyuk Park (박진혁, Hongik University, MS '23), currently at Nota AI </li>
<li> Haonan Yang (양호남, Hongik University, MS '22), currently at State Power Investment Corporation (중국국가전력투자공사) </li>
</ul>


## Collaborators
  <ul style="overflow: hidden">
<li><a href="http://www.math.snu.ac.kr/~ernestryu/">Ernest Ryu</a></li>
<li><a href="https://web.stanford.edu/~tsachy">Tsachy Weissman</a></li>
<li><a href="https://people.eecs.berkeley.edu/~jiantao/">Jiantao Jiao</a></li>
<li><a href="https://people.eecs.berkeley.edu/~courtade">Thomas Courtade</a></li>
<li><a href="http://idoia.ece.illinois.edu/">Idoia Ochoa</a></li>
<li><a href="http://mikelhernaez.github.io/">Mikel Hernaez</a></li>
<li><a href="https://idsl.seoultech.ac.kr/">Hyun Kim</a></li>
</ul>
