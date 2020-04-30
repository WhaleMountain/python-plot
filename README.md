## python で図のプロット

gnuplot の代用

### 使い方

```shell
python3 plot.py data.txt ... data5.txt
GraphName: test
xlabel: x
ylabel: y
Xrange: 0 100
Yrange: 0 100
画像を表示しますか(Y or N): n
```
test.pdf が作成される。

データの中身1列目がx軸 2列目がy軸
```txt
0 1
1 2
2 3
```
