import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

def main():
    n = 0
    n_1 = 0

    xn = []
    xn_1 = []

    st.title('Logistic Map')
    st.write('x_n+1 = a * x_n * (1 - x_n)')

    times = st.number_input('計算回数を入力してください？?', min_value=1, max_value=1000)
    a = st.number_input('定数aの値を入力してください', min_value=0.01, max_value=10.00)
    x0 = st.number_input('初期値x0の値を入力してください', min_value=0.01, max_value=10.00)

    if st.button('Calculate'):
        for i in range(times):
            if i == 0:
                xn.append(x0)
            else:
                n = a * xn[i-1] * (1 - xn[i-1])
                xn_1.append(n)
                if i != times-1:
                    xn.append(n)

        # xn を降順にソートし、それに対応して xn_1 もソートする
        xn_sorted = sorted(xn)
        xn_1_sorted = [xn_1[xn.index(x)] for x in xn_sorted]

        st.line_chart(xn)
        st.scatter_chart(pd.DataFrame(xn_1, xn))

        # 新しいxの値を生成（より滑らかな曲線を得るため）
        xnew = np.linspace(min(xn_sorted), max(xn_1_sorted), 300)

        # スプライン補間関数の作成
        spl = make_interp_spline(xn_sorted, xn_1_sorted, k=3)

        # 新しいyの値を生成
        ynew = spl(xnew)

        # 散布図のプロット
        plt.scatter(xn_sorted, xn_1_sorted, color='red', marker='o')

        # 平滑曲線をプロット
        plt.plot(xnew, ynew, color='blue')
        st.pyplot(plt)

if __name__ == '__main__':
    main()
