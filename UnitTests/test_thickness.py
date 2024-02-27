import unittest
import numpy as np
import pandas as pd
import PyIRoGlass as pig


class test_thickness(unittest.TestCase):

    def setUp(self):

        self.xfo = 0.72
        self.decimalPlace = 5
        self.wn_high_ol = 2700
        self.wn_low_ol = 2100
        self.wn_high_gl = 2850
        self.wn_low_gl = 1700
        self.wn = [1700.98, 1702.908, 1704.837, 1706.765, 1708.694, 1710.622, 1712.551, 1714.479, 1716.408, 1718.337, 1720.265, 1722.194, 1724.122, 1726.051, 1727.979, 1729.908, 1731.836, 1733.765, 1735.694, 1737.622, 1739.551, 1741.479, 1743.408, 1745.336, 1747.265, 1749.193, 1751.122, 1753.051, 1754.979, 1756.908, 1758.836, 1760.765, 1762.693, 1764.622, 1766.55, 1768.479, 1770.407, 1772.336, 1774.265, 1776.193, 1778.122, 1780.05, 1781.979, 1783.907, 1785.836, 1787.764, 1789.693, 1791.621, 1793.55, 1795.479, 1797.407, 1799.336, 1801.264, 1803.193, 1805.121, 1807.05, 1808.978, 1810.907, 1812.835, 1814.764, 1816.693, 1818.621, 1820.55, 1822.478, 1824.407, 1826.335, 1828.264, 1830.192, 1832.121, 1834.05, 1835.978, 1837.907, 1839.835, 1841.764, 1843.692, 1845.621, 1847.549, 1849.478, 1851.406, 1853.335, 1855.264, 1857.192, 1859.121, 1861.049, 1862.978, 1864.906, 1866.835, 1868.763, 1870.692, 1872.62, 1874.549, 1876.478, 1878.406, 1880.335, 1882.263, 1884.192, 1886.12, 1888.049, 1889.977, 1891.906, 1893.834, 1895.763, 1897.692, 1899.62, 1901.549, 1903.477, 1905.406, 1907.334, 1909.263, 1911.191, 1913.12, 1915.049, 1916.977, 1918.906, 1920.834, 1922.763, 1924.691, 1926.62, 1928.548, 1930.477, 1932.406, 1934.334, 1936.263, 1938.191, 1940.12, 1942.048, 1943.977, 1945.905, 1947.834, 1949.762, 1951.691, 1953.62, 1955.548, 1957.477, 1959.405, 1961.334, 1963.262, 1965.191, 1967.119, 1969.048, 1970.976, 1972.905, 1974.833, 1976.762, 1978.691, 1980.619, 1982.548, 1984.476, 1986.405, 1988.333, 1990.262, 1992.19, 1994.119, 1996.048, 1997.976, 1999.905, 2001.833, 2003.762, 2005.69, 2007.619, 2009.547, 2011.476, 2013.405, 2015.333, 2017.262, 2019.19, 2021.119, 2023.047, 2024.976, 2026.904, 2028.833, 2030.761, 2032.69, 2034.619, 2036.547, 2038.476, 2040.404, 2042.333, 2044.261, 2046.19, 2048.118, 2050.047, 2051.975, 2053.904, 2055.833, 2057.761, 2059.69, 2061.618, 2063.547, 2065.475, 2067.404, 2069.332, 2071.261, 2073.189, 2075.118, 2077.047, 2078.975, 2080.904, 2082.832, 2084.761, 2086.689, 2088.618, 2090.546, 2092.475, 2094.404, 2096.332, 2098.26, 2100.189, 2102.118, 2104.046, 2105.975, 2107.903, 2109.832, 2111.76, 2113.689, 2115.617, 2117.546, 2119.475, 2121.403, 2123.332, 2125.26, 2127.189, 2129.117, 2131.046, 2132.974, 2134.903, 2136.832, 2138.76, 2140.689, 2142.617, 2144.546, 2146.474, 2148.403, 2150.331, 2152.26, 2154.188, 2156.117, 2158.046, 2159.974, 2161.903, 2163.831, 2165.76, 2167.688, 2169.617, 2171.545, 2173.474, 2175.403, 2177.331, 2179.26, 2181.188, 2183.117, 2185.045, 2186.974, 2188.902, 2190.831, 2192.76, 2194.688, 2196.616, 2198.545, 2200.474, 2202.402, 2204.331, 2206.259, 2208.188, 2210.116, 2212.045, 2213.973, 2215.902, 2217.831, 2219.759, 2221.688, 2223.616, 2225.545, 2227.473, 2229.402, 2231.33, 2233.259, 2235.188, 2237.116, 2239.045, 2240.973, 2242.902, 2244.83, 2246.759, 2248.687, 2250.616, 2252.544, 2254.473, 2256.402, 2258.33, 2260.259, 2262.187, 2264.116, 2266.044, 2267.973, 2269.901, 2271.83, 2273.759, 2275.687, 2277.615, 2279.544, 2281.473, 2283.401, 2285.33, 2287.258, 2289.187, 2291.115, 2293.044, 2294.972, 2296.901, 2298.83, 2300.758, 2302.687, 2304.615, 2306.544, 2308.472, 2310.401, 2312.329, 2314.258, 2316.187, 2318.115, 2320.044, 2321.972, 2323.901, 2325.829, 2327.758, 2329.686, 2331.615, 2333.543, 2335.472, 2337.401, 2339.329, 2341.258, 2343.186, 2345.115, 2347.043, 2348.972, 2350.9, 2352.829, 2354.758, 2356.686, 2358.615, 2360.543, 2362.472, 2364.4, 2366.329, 2368.257, 2370.186, 2372.115, 2374.043, 2375.971, 2377.9, 2379.829, 2381.757, 2383.686, 2385.614, 2387.543, 2389.471, 2391.4, 2393.328, 2395.257, 2397.186, 2399.114, 2401.043, 2402.971, 2404.9, 2406.828, 2408.757, 2410.685, 2412.614, 2414.542, 2416.471, 2418.4, 2420.328, 2422.257, 2424.185, 2426.114, 2428.042, 2429.971, 2431.899, 2433.828, 2435.757, 2437.685, 2439.614, 2441.542, 2443.471, 2445.399, 2447.328, 2449.256, 2451.185, 2453.114, 2455.042, 2456.97, 2458.899, 2460.828, 2462.756, 2464.685, 2466.613, 2468.542, 2470.47, 2472.399, 2474.327, 2476.256, 2478.185, 2480.113, 2482.042, 2483.97, 2485.899, 2487.827, 2489.756, 2491.684, 2493.613, 2495.542, 2497.47, 2499.399, 2501.327, 2503.256, 2505.184, 2507.113, 2509.042, 2510.97, 2512.898, 2514.827, 2516.756, 2518.684, 2520.613, 2522.541, 2524.47, 2526.398, 2528.327, 2530.255, 2532.184, 2534.113, 2536.041, 2537.97, 2539.898, 2541.827, 2543.755, 2545.684, 2547.612, 2549.541, 2551.469, 2553.398, 2555.327, 2557.255, 2559.184, 2561.112, 2563.041, 2564.969, 2566.898, 2568.826, 2570.755, 2572.684, 2574.612, 2576.541, 2578.469, 2580.398, 2582.326, 2584.255, 2586.183, 2588.112, 2590.041, 2591.969, 2593.897, 2595.826, 2597.755, 2599.683, 2601.612, 2603.54, 2605.469, 2607.397, 2609.326, 2611.254, 2613.183, 2615.112, 2617.04, 2618.969, 2620.897, 2622.826, 2624.754, 2626.683, 2628.611, 2630.54, 2632.469, 2634.397, 2636.326, 2638.254, 2640.183, 2642.111, 2644.04, 2645.968, 2647.897, 2649.825, 2651.754, 2653.683, 2655.611, 2657.54, 2659.468, 2661.397, 2663.325, 2665.254, 2667.182, 2669.111, 2671.04, 2672.968, 2674.896, 2676.825, 2678.754, 2680.682, 2682.611, 2684.539, 2686.468, 2688.396, 2690.325, 2692.253, 2694.182, 2696.111, 2698.039, 2699.968, 2701.896, 2703.825, 2705.753, 2707.682, 2709.61, 2711.539, 2713.468, 2715.396, 2717.325, 2719.253, 2721.182, 2723.11, 2725.039, 2726.967, 2728.896, 2730.824, 2732.753, 2734.682, 2736.61, 2738.539, 2740.467, 2742.396, 2744.324, 2746.253, 2748.181, 2750.11, 2752.039, 2753.967, 2755.896, 2757.824, 2759.753, 2761.681, 2763.61, 2765.538, 2767.467, 2769.396, 2771.324, 2773.252, 2775.181, 2777.11, 2779.038, 2780.967, 2782.895, 2784.824, 2786.752, 2788.681, 2790.609, 2792.538, 2794.467, 2796.395, 2798.324, 2800.252, 2802.181, 2804.109, 2806.038, 2807.966, 2809.895, 2811.823, 2813.752, 2815.681, 2817.609, 2819.538, 2821.466, 2823.395, 2825.323, 2827.252, 2829.18, 2831.109, 2833.038, 2834.966, 2836.895, 2838.823, 2840.752, 2842.68, 2844.609, 2846.537, 2848.466]
        self.abs = [1.020583, 1.011716, 1.010056, 1.010377, 1.01109, 1.01478, 1.021225, 1.02853, 1.036822, 1.040173, 1.036704, 1.035069, 1.034098, 1.030995, 1.028955, 1.028164, 1.029473, 1.033651, 1.030728, 1.027346, 1.03133, 1.034971, 1.038951, 1.043997, 1.050308, 1.056206, 1.060613, 1.061516, 1.062982, 1.065469, 1.066341, 1.06847, 1.068917, 1.066218, 1.066792, 1.0686, 1.069874, 1.072113, 1.069908, 1.066861, 1.067117, 1.067561, 1.066882, 1.066389, 1.064733, 1.062884, 1.063042, 1.064721, 1.063323, 1.058671, 1.056164, 1.054663, 1.052353, 1.048931, 1.04593, 1.043769, 1.042052, 1.040526, 1.039781, 1.039386, 1.039178, 1.039037, 1.040518, 1.042439, 1.044709, 1.04567, 1.046169, 1.045685, 1.041935, 1.038376, 1.035641, 1.032046, 1.028237, 1.026454, 1.026736, 1.024038, 1.021191, 1.021212, 1.022158, 1.023441, 1.024343, 1.025538, 1.027184, 1.027247, 1.025841, 1.024786, 1.023503, 1.021776, 1.017789, 1.013216, 1.010495, 1.008821, 1.008112, 1.007929, 1.008813, 1.010286, 1.012005, 1.014749, 1.017377, 1.018534, 1.018864, 1.018449, 1.016461, 1.012964, 1.009051, 1.004576, 1.000134, 0.9962914, 0.9927732, 0.9897096, 0.987771, 0.9873329, 0.9884676, 0.9899235, 0.9913505, 0.9932389, 0.9934167, 0.992745, 0.9919873, 0.9900623, 0.9871353, 0.9827986, 0.9770666, 0.9717489, 0.9671019, 0.9631042, 0.9592541, 0.9561361, 0.95451, 0.9542438, 0.955349, 0.9578133, 0.9608377, 0.9631481, 0.9649014, 0.9653701, 0.9648114, 0.9633896, 0.960799, 0.9561645, 0.9515355, 0.948189, 0.9446552, 0.9412375, 0.9389811, 0.9378436, 0.9377751, 0.9390033, 0.9418982, 0.94575, 0.94978, 0.9531676, 0.9556165, 0.9579235, 0.9587322, 0.9575748, 0.9552557, 0.9515247, 0.9462699, 0.9400808, 0.9342956, 0.9298562, 0.9257731, 0.922233, 0.9203573, 0.9197055, 0.9201342, 0.9214494, 0.9226428, 0.9238961, 0.924915, 0.9245349, 0.9225941, 0.9188608, 0.9129443, 0.9058173, 0.8988603, 0.8919775, 0.8852137, 0.8795405, 0.8757873, 0.8735663, 0.8727468, 0.8738693, 0.8760529, 0.8788334, 0.882052, 0.8850312, 0.8871553, 0.8884376, 0.8885067, 0.8871244, 0.8845978, 0.8803508, 0.8752686, 0.8703328, 0.865853, 0.8625715, 0.8606236, 0.8596422, 0.859719, 0.8611996, 0.8637537, 0.8665482, 0.869262, 0.8721815, 0.8748603, 0.8771853, 0.8784955, 0.8778838, 0.8758668, 0.8732336, 0.8701192, 0.8663936, 0.8623665, 0.8588824, 0.8566167, 0.8554226, 0.8553206, 0.8561192, 0.8576086, 0.8597494, 0.8626562, 0.8655683, 0.8679856, 0.8701353, 0.8715089, 0.8719133, 0.8713134, 0.8699853, 0.8681639, 0.8652869, 0.861811, 0.8586689, 0.8559095, 0.8538229, 0.8521714, 0.8518564, 0.8528331, 0.8544457, 0.8564513, 0.858667, 0.8613505, 0.8641433, 0.8662304, 0.867592, 0.8678326, 0.867177, 0.8658627, 0.8634521, 0.8604652, 0.8572671, 0.8544174, 0.8513765, 0.8489732, 0.8474135, 0.8468698, 0.8475645, 0.8486117, 0.8506775, 0.8535439, 0.8556452, 0.8573649, 0.859121, 0.8602605, 0.8602774, 0.8592403, 0.8572187, 0.8549281, 0.8517796, 0.8482863, 0.8451973, 0.8421924, 0.8398129, 0.8383427, 0.8379127, 0.8382969, 0.8392297, 0.8407292, 0.8430046, 0.8449931, 0.8463593, 0.8475632, 0.8478963, 0.8474974, 0.8465433, 0.8442497, 0.8410665, 0.8378426, 0.834107, 0.830825, 0.8283697, 0.8262495, 0.8250093, 0.8245685, 0.8246834, 0.8252645, 0.8265327, 0.8276843, 0.8286586, 0.8295341, 0.8301092, 0.8306162, 0.8302415, 0.8286915, 0.8260401, 0.8229305, 0.8197907, 0.8167899, 0.8142602, 0.8123196, 0.8107562, 0.8094115, 0.8085777, 0.8088179, 0.8099348, 0.8107235, 0.8113704, 0.8124402, 0.8134915, 0.8139005, 0.813623, 0.8128304, 0.8114451, 0.809302, 0.8072917, 0.8055199, 0.803097, 0.8004071, 0.7984169, 0.7970756, 0.7961122, 0.7953587, 0.7954882, 0.7953625, 0.7952263, 0.7959703, 0.796712, 0.7976105, 0.79837, 0.7986351, 0.797862, 0.7962294, 0.7951571, 0.7935983, 0.7911855, 0.7891254, 0.7866024, 0.7846335, 0.783304, 0.78224, 0.7814776, 0.7812228, 0.7812294, 0.7810687, 0.7814137, 0.7821554, 0.7823824, 0.7820688, 0.781585, 0.7813405, 0.7810469, 0.7800974, 0.7785708, 0.7772884, 0.7763857, 0.775609, 0.7747612, 0.7739412, 0.7735876, 0.7735519, 0.7734414, 0.7731725, 0.7732457, 0.7739293, 0.7748923, 0.7755677, 0.775773, 0.77577, 0.775639, 0.7753621, 0.7746474, 0.7739386, 0.7735191, 0.7727962, 0.771906, 0.771325, 0.7710848, 0.7709936, 0.7708869, 0.7711281, 0.7712479, 0.7714913, 0.7720421, 0.772723, 0.7734421, 0.7743574, 0.7752358, 0.7752802, 0.7749581, 0.7748249, 0.7749072, 0.7748154, 0.7739353, 0.7731451, 0.7729153, 0.7728906, 0.7727442, 0.7725084, 0.7722375, 0.7722201, 0.7726862, 0.7737827, 0.7744998, 0.7748308, 0.7757319, 0.7764129, 0.776656, 0.777181, 0.7775484, 0.7772357, 0.7768981, 0.7766709, 0.7762403, 0.775865, 0.7757292, 0.775338, 0.7748588, 0.7748931, 0.7750075, 0.7749855, 0.7749686, 0.7756536, 0.7767604, 0.7771534, 0.7775218, 0.7784898, 0.7785904, 0.777928, 0.7776617, 0.7777568, 0.7778146, 0.7775217, 0.7772473, 0.7766877, 0.7757088, 0.7750791, 0.7747837, 0.7746765, 0.7747367, 0.7751387, 0.7756333, 0.7760683, 0.776161, 0.7760789, 0.7766979, 0.7769, 0.7763146, 0.7760199, 0.7760013, 0.7754377, 0.7750186, 0.7745423, 0.7734561, 0.7723659, 0.7718965, 0.7714956, 0.7708955, 0.7704052, 0.7699525, 0.7697388, 0.7698807, 0.7700964, 0.7704247, 0.7704611, 0.7703475, 0.770279, 0.769828, 0.7692037, 0.7683634, 0.7679303, 0.7673056, 0.7660556, 0.7649163, 0.7638579, 0.762736, 0.7616605, 0.7611527, 0.760515, 0.7599469, 0.7598943, 0.7601219, 0.7599848, 0.75993, 0.7603506, 0.7600033, 0.7591771, 0.7587984, 0.758707, 0.7584011, 0.7573321, 0.7557866, 0.7542044, 0.7527732, 0.7516828, 0.7508492, 0.7500915, 0.7496533, 0.7492396, 0.748831, 0.7488262, 0.7491466, 0.749245, 0.7493446, 0.7493286, 0.7486278, 0.7478377, 0.7472695, 0.7467049, 0.745913, 0.7447091, 0.7434441, 0.7423925, 0.7410882, 0.7399685, 0.7393751, 0.739363, 0.7394479, 0.7391173, 0.738744, 0.7389171, 0.7392328, 0.7391272, 0.7387456, 0.7382043, 0.7380476, 0.73787, 0.7372326, 0.7363828, 0.7352934, 0.7339848, 0.7329674, 0.7323452, 0.7319279, 0.7314163, 0.7310115, 0.7306527, 0.7306536, 0.7313194, 0.731777, 0.7317884, 0.7320378, 0.7319708, 0.7318103, 0.7314433, 0.7314256, 0.7316061, 0.7310449, 0.7299048, 0.728618, 0.7274098, 0.7269824, 0.7267954, 0.7261909, 0.7261261, 0.7265746, 0.7269046, 0.7269477, 0.7270696, 0.7274373, 0.7281301, 0.7288784, 0.7291965, 0.7294105, 0.7293057, 0.729311, 0.7293701, 0.7285315, 0.7274321, 0.72649, 0.725925, 0.7253935, 0.725091, 0.7249922, 0.7251455, 0.7259523, 0.7265646, 0.7268927, 0.7274462, 0.7282179, 0.7286351, 0.7287739, 0.7291151, 0.7294124, 0.7293346, 0.7290412]
        self.file = 'AC4_OL27_REF_a'
        self.df = pd.DataFrame({'Wavenumber': self.wn, 'Absorbance': self.abs})
        self.df.set_index('Wavenumber', inplace=True)
        self.dfs_dict = {self.file: self.df}
        self.dfs_dict_malformed = {"file1": "invalid data"}

    def test_reflectance_index(self):

        result = pig.reflectance_index(self.xfo)
        expected = 1.7097733333333334
        self.assertAlmostEqual(
            result,
            expected,
            self.decimalPlace,
            msg="Reflectance index test and expected values from "
            "the reflectance_index function do not agree")

    def test_calc_thickness(self):

        thickness = float(pig.calculate_thickness(
            1.7097733333333334, np.array([0, 50]))[0])
        expected_thickness = 0.00584873
        self.assertAlmostEqual(
            thickness,
            expected_thickness,
            self.decimalPlace,
            msg="Reflectance thickness test and expected values from "
            "the calculate_thickness function do not agree")

    def test_peak_identification(self):

        savgol_filter_width_ol = 99
        smoothing_wn_width_ol = 15
        peak_heigh_min_delta_ol = 0.002
        peak_search_width_ol = 10
        peaks, _ = pig.peakID(self.df, self.wn_high_ol, self.wn_low_ol,
                              filename=self.file,
                              plotting=True,
                              savgol_filter_width=savgol_filter_width_ol,
                              smoothing_wn_width=smoothing_wn_width_ol,
                              remove_baseline=True,
                              peak_heigh_min_delta=peak_heigh_min_delta_ol,
                              peak_search_width=peak_search_width_ol)
        expected_peak_loc = 2138.76
        self.assertAlmostEqual(float(peaks[0, 0]),
                               expected_peak_loc,
                               self.decimalPlace - 2,
                               msg="Peak location test and expected values "
                               "from the Peak_ID function do not agree")

    def test_process_thickness(self):

        try:
            result = pig.reflectance_index(self.xfo)
            thickness_results_ol = pig.calculate_mean_thickness(
                self.dfs_dict,
                result,
                self.wn_high_ol,
                self.wn_low_ol,
                remove_baseline=False,
                plotting=False,
                phaseol=True)

            thickness_results_gl = pig.calculate_mean_thickness(
                self.dfs_dict,
                1.546,
                self.wn_high_gl,
                self.wn_low_gl,
                remove_baseline=False,
                plotting=False,
                phaseol=False)

            result_ol = float(thickness_results_ol['Thickness_M'].iloc[0])
            expected_ol = 79.81
            result_gl = float(thickness_results_gl['Thickness_M'].iloc[0])
            expected_gl = 8.83
            self.assertAlmostEqual(
                result_ol,
                expected_ol,
                self.decimalPlace -
                2,
                msg="Olivine thickness test and expected values from "
                    "calculate_mean_thickness function disagree")
            self.assertAlmostEqual(
                result_gl,
                expected_gl,
                self.decimalPlace -
                2,
                msg="Glass thickness test and expected values from "
                    "calculate_mean_thickness function disagree")

        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")

    def test_exception_handling(self):
        with self.assertRaises(Exception):
            pig.calculate_mean_thickness(
                self.dfs_dict_malformed,
                1.546,
                self.wn_high_ol,
                self.wn_low_ol,
                remove_baseline=True,
                plotting=False,
                phaseol=True
            )

if __name__ == '__main__':
    unittest.main()
