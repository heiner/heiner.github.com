import os
import re
import urllib.request
import time
import zipfile

import numpy as np

FF3F = (  # Monthly data.
    "https://mba.tuck.dartmouth.edu/pages/faculty/"
    "ken.french/ftp/F-F_Research_Data_Factors_TXT.zip"
)


def download(url=FF3F):
    archive = os.path.basename(url)
    if not os.path.exists(archive):
        print("Retrieving", url)
        urllib.request.urlretrieve(url, archive)
    return archive


def extract(archive, match=re.compile(rb"\d" * 6)):
    with zipfile.ZipFile(archive) as z:
        name, *rest = z.namelist()
        assert not rest
        with z.open(name) as f:
            # Filter for the actual data lines in the file.
            return np.loadtxt((line for line in f if match.match(line)), unpack=True)


date, mktmrf, _, _, rf = extract(download())

mkt = mktmrf + rf

A = np.stack([np.ones_like(mktmrf), mktmrf], axis=1)
alpha, beta = np.linalg.inv(A.T @ A) @ A.T @ (0.6 * mkt + 0.4 * rf - rf)
print("alpha=%f; beta=%f" % (alpha, beta))


# Second part: Get some fund data.

IJS = (
    "https://gist.githubusercontent.com/heiner/b222d0985cbebfdfc77288404e6b2735/"
    "raw/08c1cacecbcfcd9e30ce28ee6d3fe3d96c07115c/IJS.csv"
)


def extract_csv(archive):
    with open(archive) as f:
        return np.loadtxt(
            f,
            delimiter=",",
            skiprows=1,  # Header.
            converters={  # Hacky date handling.
                0: lambda s: time.strftime(
                    "%Y%m", time.strptime(s.decode("ascii"), "%Y-%m-%d")
                )
            },
        )


ijs_data = extract_csv(download(IJS))

ijs = ijs_data[:, 5]  # Adj Close (includes dividends).

# Turn into monthly percentage returns.
ijs = 100 * (ijs[1:] / ijs[:-1] - 1)
ijs_date = ijs_data[1:, 0]

ijs_date, indices, ijs_indices = np.intersect1d(date, ijs_date, return_indices=True)

# Regression model for CAPM.
A = np.stack([np.ones_like(ijs_date), mktmrf[indices]], axis=1)
y = ijs[ijs_indices] - rf[indices]
B = np.linalg.inv(A.T @ A) @ A.T @ y
alpha, beta = B

# R^2 and adjusted R^2.
model_err = A @ B - y
ss_err = model_err.T @ model_err
r2 = 1 - ss_err.item() / np.var(y, ddof=len(y) - 1)
adjr2 = 1 - ss_err.item() / (A.shape[0] - A.shape[1]) / np.var(y, ddof=1)

print(
    "CAPM: alpha=%.2f%%; beta=%.2f. R^2=%.1f%%; R_adj^2=%.1f%%. Annualized alpha: %.2f%%"
    % (
        alpha,
        beta,
        100 * r2,
        100 * adjr2,
        ((1 + alpha / 100) ** 12 - 1) * 100,
    )
)

date, mktmrf, smb, hml, rf = extract(download())

orig_indices = (196307 <= date) & (date <= 199112)
assert len(smb[orig_indices]) == 342
print(np.corrcoef(smb[orig_indices], hml[orig_indices]))


A = np.stack(
    [np.ones_like(ijs_date), mktmrf[indices], smb[indices], hml[indices]], axis=1
)
y = ijs[ijs_indices] - rf[indices]
B = np.linalg.inv(A.T @ A) @ A.T @ y
alpha, beta_mkt, beta_smb, beta_hml = B

model_err = A @ B - y
ss_err = model_err.T @ model_err
r2 = 1 - ss_err.item() / np.var(y, ddof=len(y) - 1)
adjr2 = 1 - ss_err.item() / (A.shape[0] - A.shape[1]) / np.var(y, ddof=1)

print(
    "FF3F: alpha=%.2f%%; beta_mkt=%.2f; beta_smb=%.2f; beta_hml=%.2f."
    " R^2=%.1f%%; R_adj^2=%.1f%%. Annualized alpha: %.2f%%"
    % (
        alpha,
        beta_mkt,
        beta_smb,
        beta_hml,
        100 * r2,
        100 * adjr2,
        ((1 + alpha / 100) ** 12 - 1) * 100,
    )
)
