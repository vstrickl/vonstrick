import React from "react"
import { graphql } from "gatsby"

import "../styles/styles.scss"

export default function IndexPage ({data}) {
  const { markdownRemark } = data
  const { frontmatter, html } = markdownRemark
  return <div class="container">
    <div class="header">
      <div class="full-name">
        <span class="first-name">{frontmatter.first}</span>
        <span class="last-name">{frontmatter.last}</span>
      </div>
      <h1>{frontmatter.job}</h1>
      <div class="contact-info">
        <span class="email-val"><a href={"mailto:" + frontmatter.email}>{frontmatter.email}</a></span>
        <p>{frontmatter.location}</p>
      </div>
      <div
          dangerouslySetInnerHTML={{ __html: html }}
        />
    </div>
   
  </div>
}

export const pageQuery = graphql`
  query{
    markdownRemark(frontmatter: {slug: {eq: "/resume"}}) {
      frontmatter {
        first
        last
        job
        location
        email
      }
      html
    }
  }
`