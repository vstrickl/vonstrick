exports.createPages = async ({ actions, graphql, reporter }) => {
    const { createPage } = actions
  
    const resumeTemplate = require.resolve(`./src/pages/index.js`)
    const portfolioTemplate = require.resolve(`./src/pages/portfolio.js`)
  
    const result = await graphql(`
      {
        allMarkdownRemark(
          sort: { order: DESC, fields: [frontmatter___title] }
          limit: 1000
        ) {
          edges {
            node {
              frontmatter {
                slug
              }
            }
          }
        }
      }
    `)
  
    // Handle errors
    if (result.errors) {
      reporter.panicOnBuild(`Error while running GraphQL query.`)
      return
    }

    // Create Resume Home Page
    result.data.allMarkdownRemark.edges.forEach(({ node }) => {
      createPage({
        path: node.frontmatter.slug,
        component: resumeTemplate,
        context: {
          // additional data can be passed via context
          slug: node.frontmatter.slug,
        },
      })
    })

    // Create Portfolio Page
    result.data.allMarkdownRemark.edges.forEach(({ node }) => {
      createPage({
        path: node.frontmatter.slug,
        component: portfolioTemplate,
        context: {
          // additional data can be passed via context
          slug: node.frontmatter.slug,
        },
      })
    })
  }