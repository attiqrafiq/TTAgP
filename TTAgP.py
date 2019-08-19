import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "untitled.ui"  #Name of the file here

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.bottonpred_2.clicked.connect(self.calculation) 

    def calculation(self):

        from sklearn.externals import joblib

        rfc = joblib.load('modelo_entrenado_9.pkl')

        # Data entry

        paste_seq = str(self.pasteseq_2.toPlainText())

        # Computing
        kyte_doolittle = {'A': 1.80, 'C': 2.50, 'D': -3.50, 'E': -3.50, 'F': 2.80,
                          'G': -0.40, 'H': -3.20, 'I': 4.50, 'K': -3.90, 'L': 3.80,
                          'M': 1.90, 'N': -3.50, 'P': -1.60, 'Q': -3.50, 'R': -4.50,
                          'S': -0.80, 'T': -0.70, 'V': 4.20, 'W': -0.90, 'Y': -1.30}

        net_charge = {'A': 0, 'C': 0, 'D': -1, 'E': -1, 'F': 0,
                      'G': 0, 'H': 0, 'I': 0, 'K': 1, 'L': 0,
                      'M': 0, 'N': 0, 'P': 0, 'Q': 0, 'R': 1,
                      'S': 0, 'T': 0, 'V': 0, 'W': 0, 'Y': 0}

        net_hydrogen = {'A': 0, 'C': 0, 'D': 1, 'E': 1, 'F': 0,
                        'G': 0, 'H': 1, 'I': 0, 'K': 2, 'L': 0,
                        'M': 0, 'N': 2, 'P': 0, 'Q': 2, 'R': 4,
                        'S': 1, 'T': 1, 'V': 0, 'W': 1, 'Y': 1}

        a_a = round(paste_seq.count("A")/len(paste_seq+str(0.000001)), 3)
        c_c = round(paste_seq.count("C")/len(paste_seq+str(0.000001)), 3)
        d_d = round(paste_seq.count("D")/len(paste_seq+str(0.000001)), 3)
        e_e = round(paste_seq.count("E")/len(paste_seq+str(0.000001)), 3)
        f_f = round(paste_seq.count("F")/len(paste_seq+str(0.000001)), 3)
        g_g = round(paste_seq.count("G")/len(paste_seq+str(0.000001)), 3)
        h_h = round(paste_seq.count("H")/len(paste_seq+str(0.000001)), 3)
        i_i = round(paste_seq.count("I")/len(paste_seq+str(0.000001)), 3)
        k_k = round(paste_seq.count("K")/len(paste_seq+str(0.000001)), 3)
        l_l = round(paste_seq.count("L")/len(paste_seq+str(0.000001)), 3)
        m_m = round(paste_seq.count("M")/len(paste_seq+str(0.000001)), 3)
        n_n = round(paste_seq.count("N")/len(paste_seq+str(0.000001)), 3)
        p_p = round(paste_seq.count("P")/len(paste_seq+str(0.000001)), 3)
        q_q = round(paste_seq.count("Q")/len(paste_seq+str(0.000001)), 3)
        r_r = round(paste_seq.count("R")/len(paste_seq+str(0.000001)), 3)
        s_s = round(paste_seq.count("S")/len(paste_seq+str(0.000001)), 3)
        t_t = round(paste_seq.count("T")/len(paste_seq+str(0.000001)), 3)
        v_v = round(paste_seq.count("V")/len(paste_seq+str(0.000001)), 3)
        w_w = round(paste_seq.count("W")/len(paste_seq+str(0.000001)), 3)
        y_y = round(paste_seq.count("Y")/len(paste_seq+str(0.000001)), 3)

        a_kyte = paste_seq.count("A")*kyte_doolittle["A"]
        c_kyte = paste_seq.count("C")*kyte_doolittle["C"]
        d_kyte = paste_seq.count("D")*kyte_doolittle["D"]
        e_kyte = paste_seq.count("E")*kyte_doolittle["E"]
        f_kyte = paste_seq.count("F")*kyte_doolittle["F"]
        g_kyte = paste_seq.count("G")*kyte_doolittle["G"]
        h_kyte = paste_seq.count("H")*kyte_doolittle["H"]
        i_kyte = paste_seq.count("I")*kyte_doolittle["I"]
        k_kyte = paste_seq.count("K")*kyte_doolittle["K"]
        l_kyte = paste_seq.count("L")*kyte_doolittle["L"]
        m_kyte = paste_seq.count("M")*kyte_doolittle["M"]
        n_kyte = paste_seq.count("N")*kyte_doolittle["N"]
        p_kyte = paste_seq.count("P")*kyte_doolittle["P"]
        q_kyte = paste_seq.count("Q")*kyte_doolittle["Q"]
        r_kyte = paste_seq.count("R")*kyte_doolittle["R"]
        s_kyte = paste_seq.count("S")*kyte_doolittle["S"]
        t_kyte = paste_seq.count("T")*kyte_doolittle["T"]
        v_kyte = paste_seq.count("V")*kyte_doolittle["V"]
        w_kyte = paste_seq.count("W")*kyte_doolittle["W"]
        y_kyte = paste_seq.count("Y")*kyte_doolittle["Y"]

        a_charge = paste_seq.count("A")*net_charge["A"]
        c_charge = paste_seq.count("C")*net_charge["C"]
        d_charge = paste_seq.count("D")*net_charge["D"]
        e_charge = paste_seq.count("E")*net_charge["E"]
        f_charge = paste_seq.count("F")*net_charge["F"]
        g_charge = paste_seq.count("G")*net_charge["G"]
        h_charge = paste_seq.count("H")*net_charge["H"]
        i_charge = paste_seq.count("I")*net_charge["I"]
        k_charge = paste_seq.count("K")*net_charge["K"]
        l_charge = paste_seq.count("L")*net_charge["L"]
        m_charge = paste_seq.count("M")*net_charge["M"]
        n_charge = paste_seq.count("N")*net_charge["N"]
        p_charge = paste_seq.count("P")*net_charge["P"]
        q_charge = paste_seq.count("Q")*net_charge["Q"]
        r_charge = paste_seq.count("R")*net_charge["R"]
        s_charge = paste_seq.count("S")*net_charge["S"]
        t_charge = paste_seq.count("T")*net_charge["T"]
        v_charge = paste_seq.count("V")*net_charge["V"]
        w_charge = paste_seq.count("W")*net_charge["W"]
        y_charge = paste_seq.count("Y")*net_charge["Y"]

        a_hydrogen = paste_seq.count("A")*net_hydrogen["A"]
        c_hydrogen = paste_seq.count("C")*net_hydrogen["C"]
        d_hydrogen = paste_seq.count("D")*net_hydrogen["D"]
        e_hydrogen = paste_seq.count("E")*net_hydrogen["E"]
        f_hydrogen = paste_seq.count("F")*net_hydrogen["F"]
        g_hydrogen = paste_seq.count("G")*net_hydrogen["G"]
        h_hydrogen = paste_seq.count("H")*net_hydrogen["H"]
        i_hydrogen = paste_seq.count("I")*net_hydrogen["I"]
        k_hydrogen = paste_seq.count("K")*net_hydrogen["K"]
        l_hydrogen = paste_seq.count("L")*net_hydrogen["L"]
        m_hydrogen = paste_seq.count("M")*net_hydrogen["M"]
        n_hydrogen = paste_seq.count("N")*net_hydrogen["N"]
        p_hydrogen = paste_seq.count("P")*net_hydrogen["P"]
        q_hydrogen = paste_seq.count("Q")*net_hydrogen["Q"]
        r_hydrogen = paste_seq.count("R")*net_hydrogen["R"]
        s_hydrogen = paste_seq.count("S")*net_hydrogen["S"]
        t_hydrogen = paste_seq.count("T")*net_hydrogen["T"]
        v_hydrogen = paste_seq.count("V")*net_hydrogen["V"]
        w_hydrogen = paste_seq.count("W")*net_hydrogen["W"]
        y_hydrogen = paste_seq.count("Y")*net_hydrogen["Y"]

        # PROPERTIES Q-P

        aliphatic = round((i_i + l_l + v_v), 3)

        negative_charged = round((d_d + e_e), 3)

        total_charged = round((d_d + e_e + k_k + h_h + r_r), 3)

        aromatic = round((f_f + h_h + w_w + y_y), 3)

        polar = round((d_d + e_e + r_r + k_k + q_q + n_n), 3)

        neutral = round((a_a + g_g + h_h + p_p + s_s + t_t + y_y), 3)

        hydrophobic = round((c_c + f_f + i_i + l_l + m_m + v_v + w_w), 3)

        positive_charged = round((k_k + r_r + h_h), 3)

        tiny = round((a_a + c_c + d_d + g_g + s_s + t_t), 3)

        small = round((e_e + h_h + i_i + l_l + k_k + m_m + n_n + p_p + q_q + v_v), 3)

        large = round((f_f + r_r + w_w + y_y), 3)

        # SCALES

        kyleD = round(((a_kyte+c_kyte+d_kyte+e_kyte+f_kyte+g_kyte+h_kyte+i_kyte+k_kyte+l_kyte+m_kyte+n_kyte+p_kyte+q_kyte+r_kyte+s_kyte+t_kyte+v_kyte+w_kyte+y_kyte)/len(paste_seq+str(0.000001))),3)

        netCharge = a_charge+c_charge+d_charge+e_charge+f_charge+g_charge+h_charge+i_charge+k_charge+l_charge+m_charge+n_charge+p_charge+q_charge+r_charge+s_charge+t_charge+v_charge+w_charge+y_charge

        netH = round((a_hydrogen+c_hydrogen+d_hydrogen+e_hydrogen+f_hydrogen+g_hydrogen+h_hydrogen+i_hydrogen+k_hydrogen+l_hydrogen+m_hydrogen+n_hydrogen+p_hydrogen+q_hydrogen+r_hydrogen+s_hydrogen+t_hydrogen+v_hydrogen+w_hydrogen+y_hydrogen),3)

        result = "Probable: " + str(rfc.predict([[netH,netCharge,kyleD,a_a,c_c,d_d,e_e,f_f,g_g,h_h,i_i,k_k,l_l,m_m,n_n,p_p,q_q,r_r,s_s,t_t,v_v,w_w,y_y,tiny,small,large,aliphatic,aromatic,total_charged,negative_charged,positive_charged,polar,neutral,hydrophobic]]))

        self.textpred_2.setText(str(result))
        self.textpred1_2.setText(str(aliphatic))
        self.textpred2_2.setText(str(negative_charged))
        self.textpred3_2.setText(str(aromatic))
        self.textpred4_2.setText(str(polar))
        self.textpred5_2.setText(str(neutral))
        self.textpred6_2.setText(str(hydrophobic))
        self.textpred7_2.setText(str(positive_charged))
        self.textpred8_2.setText(str(tiny))
        self.textpred9_2.setText(str(small))
        self.textpred10_2.setText(str(large))
        self.textpred11_2.setText(str(kyleD))
        self.textpred13_2.setText(str(netCharge))
        self.textpred14_2.setText(str(netH))
        self.textpred15_2.setText(str(total_charged))
        self.textrelat_2.setText("A: " + str(a_a) + " , " + "C: " + str(c_c) + " , " + "D: " + str(d_d) + " , " + "E: " + str(e_e) + " , " + "F: " + str(f_f) + " , " + "E: " + str(e_e) + " , " + "G: " + str(g_g) + " , " + "I: " + str(i_i) + " , " + "K: " + str(k_k) + " , " + "L: " + str(l_l) + " , " + "M: " + str(m_m) + " , " + "N: " + str(n_n) + " , " + "P: " + str(p_p) + " , " + "Q: " + str(q_q) + " , " + "R: " + str(r_r) + " , " + "S: " + str(s_s) + " , " + "T: " + str(t_t) + " , " + "V: " + str(v_v) + " , " + "W: " + str(w_w) + " , " + "Y: " + str(y_y))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
