import React from "react"
import { graphql } from "gatsby"

import "../styles/styles.scss"

export default function PortfolioPage ({data}){
  const { markdownRemark } = data
  const { frontmatter, html } = markdownRemark
  return <div class="container">
    <div class="header">
      <div class="full-name">
        <span class="first-name">{frontmatter.first}</span>
        <span class="last-name">{frontmatter.last}</span>
      </div>
      <div
          dangerouslySetInnerHTML={{ __html: html }}
        />
    </div>
  </div>
}

export const pageQuery = graphql`
  query{
    markdownRemark(frontmatter: {slug: {eq: "/portfolio"}}) {
      frontmatter {
        first
        last
      }
      html
    }
  }
`