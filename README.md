# README

Punk API is a public API service that serves beer information worldwide. It is a useful resource for developers who are working on beer-related apps, websites, and other projects.

```
http://127.0.0.1:5000/v3/ – base url
```

There are several endpoints that Punk API provides
```
/random – retrieve a random beer in shortcase
/beer?id={id} – retrieve a single beer by its id in detail case
/beers?page={page_number} – retrieve a list of all the beers in short case with paging, by default 30 items per page
/img/{id}.png – retrieve the image according to specified beer id
```

Additional query parameters for `/beers`
```
per_page – set the size of paging, available from 10 to 80, 30 by default

ids={id,id,...} – retrieve a list of beers that match the specified ids
beer_name={string} – retrieve a list of beers that match the specified string

brewed_before={string} – retrieve a list of beers that have brewed date less than the specified date
brewed_after={string} – retrieve a list of beers that have brewed date greater than the specified date
abv_gt={number} – retrieve a list of beers that have an ABV greater than the specified number
abv_lt={number} – retrieve a list of beers that have an ABV less than the specified number

ibu_gt={number} – retrieve a list of beers that have an IBU greater than the specified number
ibu_lt={number} – retrieve a list of beers that have an IBU less than the specified number
ebc_gt={number} – retrieve a list of beers that have an EBC greater than the specified number
ebc_lt={number} – retrieve a list of beers that have an EBC less than the specified number
food={string} – retrieve a list of beers that go well with the specified food
```
