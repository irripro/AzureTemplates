appID="<Your_CSP_AppID>"
secret="<Your_CSP_AppID_Secret>"

csptoken=$(curl --request POST \
  --url 'https://login.windows.net/testtestcsp1twwp1.onmicrosoft.com/oauth2/token?api-version=1.0' \
  --header 'accept: application/json' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data "grant_type=client_credentials&resource=https%3A%2F%2Fgraph.windows.net&client_id=${appID}&client_secret=${secret}")

csptoken=$(echo $csptoken | jq .access_token | awk -F '"' '{print $2}')

csp_final_token=$(curl --request POST \
  --url https://api.partnercenter.microsoft.com/generatetoken \
  --header 'accept: application/json' \
  --header "authorization: Bearer ${csptoken}" \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data grant_type=jwt_token)

csp_autherization_token=$(echo $csp_final_token | jq .access_token | awk -F '"' '{print $2}')
#echo $csp_autherization_token


curl -X GET --header 'Accept: application/json' \
        --header "authorization: Bearer ${csptoken}" \
        'https://api.partnercenter.microsoft.com/v1.0/customers' | \
        jq '.items[] | "\(.companyProfile.companyName) \(.companyProfile.domain) \(.companyProfile.tenantId)"'
