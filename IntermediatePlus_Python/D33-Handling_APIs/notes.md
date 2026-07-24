## 📌 API Notes: Basics & Exception Handling

### What is an API?

An **Application Programming Interface (API)** is a set of rules, protocols, and tools that allows one software application to communicate with another or interact with external data sources.

### What is an API Endpoint?

An **API Endpoint** is a specific digital location—usually a URL—where an API receives requests and returns data.

* **Example:** `[http://api.open-notify.org/iss-now.json](http://api.open-notify.org/iss-now.json)` is an endpoint that returns the real-time position of the International Space Station (ISS).

---

### HTTP Response Status Codes

When you make a request to an API, the server sends back a 3-digit **status code** indicating the outcome of the request:

| Code Range | Category | General Meaning | Common Examples |
| --- | --- | --- | --- |
| **`1xx`** | **Informational** | Request received; process ongoing ("Hold on"). | `100 Continue` |
| **`2xx`** | **Success** | Request succeeded ("Here you go"). | `200 OK`, `201 Created` |
| **`3xx`** | **Redirection** | Further action needed to complete request ("Go away / Move elsewhere"). | `301 Moved Permanently` |
| **`4xx`** | **Client Error** | The client made an invalid request ("You screwed up"). | `401 Unauthorized`, `404 Not Found` |
| **`5xx`** | **Server Error** | The server failed to fulfill a valid request ("I screwed up"). | `500 Internal Server Error`, `503 Service Unavailable` |

---

### Handling Errors in Python (`requests`)

Checking every possible status code manually using `if`/`elif` statements is inefficient. Instead, Python's `requests` library provides a built-in method:

```python
response.raise_for_status()

```

* If the request is successful (`200 OK`), `raise_for_status()` does nothing and execution continues.
* If the server returns an error (`4xx` or `5xx`), it automatically raises an `HTTPError` exception with the proper error message.
