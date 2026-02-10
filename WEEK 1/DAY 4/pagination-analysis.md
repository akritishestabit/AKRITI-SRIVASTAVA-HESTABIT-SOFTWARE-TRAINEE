# Pagination Analysis – GitHub Repositories API

## API Endpoint Used
GET https://api.github.com/users/octocat/repos?page=1&per_page=5

## Pagination Parameters
- page = 1  
- per_page = 5 (limits number of repositories per response)

## Link Header Observation
The response contains the following Link header:

<https://api.github.com/user/583231/repos?page=2&per_page=5>; rel="next", 
<https://api.github.com/user/583231/repos?page=2&per_page=5>; rel="last"

## Meaning of Link Relations
- rel="next" → URL for the next page of results
- rel="last" → URL for the last available page

## How Pagination Works
- GitHub does not send all repositories in one response
- Data is split into pages to reduce payload size
- Client uses Link headers to navigate between pages

## Why Pagination Is Important
- Prevents large responses that slow down APIs
- Reduces memory and bandwidth usage
- Improves API scalability and performance

## Rate Limit Impact
Each paginated request consumes one rate-limit unit, which is visible via:
x-ratelimit-used and x-ratelimit-remaining headers.

## Conclusion
Pagination ensures efficient data transfer and allows clients to safely
navigate large datasets using standardized HTTP headers.
