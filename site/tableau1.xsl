<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" indent="yes"/>

  <xsl:template match="/">
      <html>
          <head>
              <meta charset="utf-8"/>
              <title>Visu XSLT</title>
              <meta name="viewport" content="width=device-width, initial-scale=1" />
              <!--[if lte IE 8]><script src="assets/js/ie/html5shiv.js"></script><![endif]-->
              <link rel="stylesheet" href="assets/css/main.css" />
          </head>
          <body>
            <!-- Header -->
      				<div id="header-wrapper">
      					<header id="header" class="container">

      						<!-- Logo -->
      							<div id="logo">
      								<h1><a href="index.html">geoapplide</a></h1>
      								<span>projet</span>
      							</div>

      							<!-- Nav -->
      								<nav id="nav">
      									<ul>
      										<li><a href="index.html">Bienvenue !</a></li>
      										<li><a href="page1_donnees.html">Données</a></li>
      										<!-- <li>
      											<a href="page1_donnees.html">Données</a>
      											<ul>
      												<li><a href="#">Lorem ipsum dolor</a></li>
      												<li><a href="#">Magna phasellus</a></li>
      												<li><a href="#">Phasellus consequat</a></li>
      												<li><a href="#">Veroeros feugiat</a></li>
      											</ul>
      										</li> -->
      										<li><a href="page2_graphes.html">Graphes</a></li>
      										<li><a href="page3_avec_carte_tests.html">Carte</a></li>
      										<li><a href="page4_tableau.html">Tableau</a></li>
      									</ul>
      								</nav>

      					</header>
      				</div>


              <div id="main-wrapper">
      					<div class="container">
      						<div class="row 200%">
      							<div class="4u 12u$(medium)">
      								<div id="sidebar">


                        <section>
                          <h3>Sélectionnez un arrondissement</h3>
                          <ul class="style2">
                            <li><a href="#75001">75001</a></li>
                            <li><a href="#75002">75002</a></li>
                            <li><a href="#75003">75003</a></li>
                            <li><a href="#75004">75004</a></li>
                            <li><a href="#75005">75005</a></li>
                            <li><a href="#75006">75006</a></li>
                            <li><a href="#75007">75007</a></li>
                            <li><a href="#75008">75008</a></li>
                            <li><a href="#75009">75009</a></li>
                            <li><a href="#75010">75010</a></li>
                            <li><a href="#75011">75011</a></li>
                            <li><a href="#75012">75012</a></li>
                            <li><a href="#75013">75013</a></li>
                            <li><a href="#75014">75014</a></li>
                            <li><a href="#75015">75015</a></li>
                            <li><a href="#75016">75016</a></li>
                            <li><a href="#75017">75017</a></li>
                            <li><a href="#75018">75018</a></li>
                            <li><a href="#75019">75019</a></li>
                            <li><a href="#75020">75020</a></li>
                          </ul>
                        </section>

    								</div>
    							</div>
    							<div class="8u 12u$(medium) important(medium)">
    								<div id="content">

    									<!-- Content -->

              <xsl:for-each select="/root/arrondissement">
                  <h2 id="{@num}"><xsl:value-of select="@num"/></h2>
                    <ul>
                    <xsl:for-each select="./element/nom">
                      <li><xsl:value-of select="."/><xsl:text>, </xsl:text><xsl:value-of select="../@type"/></li>
                    </xsl:for-each>
                  </ul>
              </xsl:for-each>

            </div>
          </div>
        </div>
      </div>
    </div>

          </body>
    </html>
</xsl:template>
</xsl:stylesheet>
